# import os
# import json
# import httpx  # use httpx instead of requests
# from dotenv import load_dotenv
# from fastapi import HTTPException

# from constant.prompt import prompt

# load_dotenv()
# url = os.getenv("OLLAMA_API_ENDPOINT")

# async def get_model_response(img_str):
#     try:
#         payload = {
#             "model": "gemma3:4b",
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": prompt,
#                     "images": [img_str]
#                 }
#             ],
#             "stream": False
#         }

#         if not url:
#             raise ValueError("OLLAMA_API_ENDPOINT is not set")

#         async with httpx.AsyncClient() as client:
#             response = await client.post(url, json=payload)

#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 if "message" in data and "content" in data["message"]:
#                     return data["message"]["content"]
#                 else:
#                     raise HTTPException(status_code=500, detail="Malformed response from model")
#             except json.JSONDecodeError:
#                 raise HTTPException(status_code=500, detail="Failed to decode response JSON")
#         else:
#             raise HTTPException(status_code=response.status_code, detail=response.text)

#     except Exception as e:
#         print(f"Error while getting ollama response: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))










import os
import json
import requests
from dotenv import load_dotenv
from fastapi import HTTPException

from constant.prompt import prompt

load_dotenv()
url = os.getenv("OLLAMA_API_ENDPOINT")

async def get_model_response(img_str):
    try:
        payload = {
            "model": "gemma3:4b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                    "images": [img_str] 
                }
            ],
            "stream": False  # Correct: Full response at once
        }

        if not url:
            raise ValueError("OLLAMA_API_ENDPOINT is not set")

        response = requests.post(url, json=payload)  # No need for stream=True

        if response.status_code == 200:
            try:
                data = response.json()
                if "message" in data and "content" in data["message"]:
                    return data["message"]["content"]
                else:
                    raise HTTPException(status_code=500, detail="Malformed response from model")
            except json.JSONDecodeError:
                raise HTTPException(status_code=500, detail="Failed to decode response JSON")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except Exception as e:
        print(f"Error while getting ollama response: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))








# # import os
# # import json
# # import requests
# # from dotenv import load_dotenv
# # from fastapi import HTTPException

# # from constant.prompt import prompt

# # load_dotenv()

# # url = os.getenv("OLLAMA_API_ENDPOINT")

# # async def get_model_response(img_str):
# #     try:
# #         payload = {
# #             "model": "gemma3:4b",
# #             "messages": [
# #                 {
# #                     "role": "user",
# #                     "content": prompt,
# #                     "images": [img_str] 
# #                 }
# #             ],
# #             "stream":False
# #         }

# #         if url:
# #             response = requests.post(url, json=payload, stream=True)
# #             print("response from ollama:------------->",response)
# #         else:
# #             print("Provide api endpoint for Ollama")

# #         if response.status_code == 200:
# #             result = ""
# #             for line in response.iter_lines(decode_unicode=True):
# #                 if line:
# #                     try:
# #                         data = await json.loads(line)
# #                         if "message" in data and "content" in data["message"]:
# #                             result += data["message"]["content"]
# #                     except json.JSONDecodeError:
# #                         result += "\n[Invalid response line]\n"
# #             return result
# #         else:
# #             raise HTTPException(status_code=response.status_code, detail=response.text)
    
# #     except Exception as e:
# #         print(f"Error while getting ollama response: {str(e)}")