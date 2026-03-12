from openai import OpenAI
import os
from constant.prompt import prompt

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_AI_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"  # ← key difference
)

def call_qwen3_vl_30b_a3b_i(base64_image):
    response = client.chat.completions.create(
        model="accounts/fireworks/models/qwen3-vl-30b-a3b-instruct",
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
    )
    print(f'\033[1;32m{response}\033[0m')
    return response.choices[0].message.content