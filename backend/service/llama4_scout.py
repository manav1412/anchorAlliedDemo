from groq import Groq
import base64
import os

from constant.prompt import prompt

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def call_groq(base64_image):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": prompt
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
    
    return chat_completion.choices[0].message.content