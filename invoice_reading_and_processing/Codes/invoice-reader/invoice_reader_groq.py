# Code from the Groq docs https://console.groq.com/docs/vision

from groq import Groq
import base64
import os

# TO DO: PARSING USING PROMPT
# CREATE INTERFACE


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# image_path = r"/home/neebal/Desktop/POC/anchor-allied/Training Data/Batch 2/1-2-1.png"
# image_path = r"/home/neebal/Desktop/POC/anchor-allied/Sample_PO/green_circle.jpg"
# image_path = r"/home/neebal/Desktop/POC/anchor-allied/Denoised_All_Samples/green_circle_method3_sharp.png"
image_path = r"/home/neebal/Desktop/POC/anchor_allied/invoice_reading_and_processing/Inputs/Denoised_Invoices/green_circle_method3_sharp.png"

# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    # "text": "You are a Image to Text converter. Print out the EXACT contents of the image. Print neatly."
                    "text": """You are an AI agent responsible for parsing unstructured text extracted from B2B invoices/bills and converting it into a fixed JSON format.

                                ## Context  
                                - The invoice format may vary but typically includes: bill number, distributor name, product list with quantity and unit price, and total cost.
                                - Output must strictly follow a specified JSON schema regardless of input variability.
                                - If any field is missing in the input, the agent should leave it blank (e.g., `""` or empty list).

                                ## Instructions  
                                1. Extract and normalize the following fields from the raw invoice text:
                                - `bill_id` (e.g., LPO number)
                                - `distributor_name` (company issuing the invoice)
                                - `products`: list of product names.
                                - `each_product_prize`: an array of objects with:
                                    - `product_name`
                                    - `quantity`
                                    - `unit_price`
                                    - `total_price` (auto-calculate if missing)
                                - `total_cost` (sum of all total prices; Calculate the total if not present)

                                2. Return the output strictly in the JSON format provided below with no explanation or text around it.

                                ```json
                                {
                                "bill_id": "",
                                "distributor_name": "",
                                "products": [],
                                "each_product_prize": [
                                    {
                                    "product_name": "",
                                    "quantity": ,
                                    "unit_price": ,
                                    "total_price": 
                                    },
                                    ...
                                ],
                                "total_cost": ""
                                }
                                """
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    # model="meta-llama/llama-4-scout-17b-16e-instruct",
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
)

print(chat_completion.choices[0].message.content)

