import os
import re
import json
import time
import base64
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pymongo import MongoClient
from PIL import Image
from io import BytesIO
from fastapi.responses import JSONResponse
from bson import ObjectId
import docx
import fitz

from service.ollama import get_model_response
from service.llama4_scout import call_groq
from service.fireworks_ai import *
from service.denoising import method3_pil_enhancement_from_base64
from service.sent_to_gsheet import send_to_google_sheets
from utils.similarity_check import fetch_similar_item

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client['allied']
collection = db['bills']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers = ["*"],
    allow_origins = ["http://localhost:5173","https://anchor-allied-demo.vercel.app"],
    allow_methods = ["*"],
    allow_credentials = True
)

@app.post('/upload')
async def upload_file(
    image: UploadFile = File(...)
):
    try:
        image_bytes = await image.read()
        image_pil = Image.open(BytesIO(image_bytes))

        # Convert image to base64
        buffered = BytesIO()
        image_pil.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Denoised base64
        enhanced_base64 = method3_pil_enhancement_from_base64(img_str)

        result = await get_model_response(enhanced_base64)
        
        print("Raw Result from ollama model:---------->",result)
        cleaned = re.sub(r"^```json\s*|\s*```$", "", result.strip())

        try:
            json_data = json.loads(cleaned)
            collection.insert_one(json_data)
            json_data["_id"] = str(json_data.get("_id", ""))
            print("Result:--------->", json_data)
            return {"response":json_data}
        except json.JSONDecodeError as e:
            print("Invalid JSON from ollama response:", e)
            return None
    
    except Exception as e:
        print(f"Error at backend route: {str(e)}")


@app.post('/upload-cloud')
async def upload_file_cloud(
    file: UploadFile = File(...)
):
    try:
        file_bytes = await file.read()
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        is_image = any(file.filename.lower().endswith(ext) for ext in image_extensions)
        if is_image:
            # Uploaded file is an image so there is no need to convert
            file_pil = Image.open(BytesIO(file_bytes))
        else:
            if file.filename.endswith('.docx'):
                # if the file is a MS Word Document, convert it to image 
                doc = docx.Document(BytesIO(file_bytes))
                # Extract first image from docx
                for rel in doc.part.rels.values():
                    if "image" in rel.target_ref:
                        img_data = rel.target_part.blob
                        file_pil = Image.open(BytesIO(img_data))
                        break
                else:
                    raise ValueError("No image found in docx")
            elif file.filename.endswith('.pdf'):
                # if the file is a PDF Document, convert it to image 
                pdf_doc = fitz.open(stream=file_bytes, filetype="pdf")
                page = pdf_doc[0]
                pix = page.get_pixmap()
                img_data = pix.tobytes("png")
                file_pil = Image.open(BytesIO(img_data))
                pdf_doc.close()
            else:
                raise NotImplementedError 

        buffered = BytesIO()
        file_pil.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # result = call_groq(img_str)
        result = call_qwen3_vl_30b_a3b_i(img_str)
        print("Raw response from qwen3:--------->", result)
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", result.strip())
        print("Cleaned Result from qwen3:---------->", cleaned)
        
        try:
            json_data = json.loads(cleaned) 
        except Exception as e:
            print("Failed to load JSON data", str(e))
                
        for i in range(len(json_data["each_product_prize"])):
            original_product_name = json_data["each_product_prize"][i]["product_name"]
            product_quantity = json_data["each_product_prize"][i]["quantity"]
            original_item_description = f"{original_product_name},{product_quantity}"
            
            similar_item, item_code = fetch_similar_item(original_item_description)
            json_data["each_product_prize"][i]["product_name"] = similar_item
            json_data["each_product_prize"][i]["item_code"] = item_code
        
        print("Json data going in DB:",json_data)
        
        insert_result = collection.insert_one(json_data)
        json_data["_id"] = str(insert_result.inserted_id)

        send_to_google_sheets(json_data)

        return {"response": json_data}

    except json.JSONDecodeError as e:
        print("Invalid JSON from cloud llm model:", e)
        return {"error": "Invalid JSON"}
        
    except Exception as e:
        return {"error": f"got error in upload-cloud api {str(e)}"}


class MongoEncoder:
    @staticmethod
    def transform(doc):
        doc["_id"] = str(doc["_id"])
        return doc


@app.get("/invoices")
def get_invoices():
    try:
        cursor = collection.find()
        invoices = [MongoEncoder.transform(doc) for doc in cursor]
        return {"invoices": invoices}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
    
@app.delete("/invoice/{invoice_id}")
def delete_invoice(
    invoice_id: str
):
    try:
        result = collection.delete_one({"_id":ObjectId(invoice_id)})
        if result.deleted_count == 0:
            return {"message":"Invoice not found"}
        return {"message": "Invoice deleted successfully"}
    except Exception as e:
        return {"error":f"Failed to delete invoice {str(e)}"}
        