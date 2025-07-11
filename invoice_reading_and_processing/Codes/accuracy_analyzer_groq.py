# Code from the Groq docs https://console.groq.com/docs/vision

from groq import Groq
import os

# TO DO: PARSING USING PROMPT
# CREATE INTERFACE

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    # "text": "You are a Image to Text converter. Print out the EXACT contents of the image. Print neatly."
                    "text": """You are an Accuracy Analyser. You will be fed with a JSON consisting of various fields and sub-fields. There is a field called product_name.
                                Your job is to check whether the Product Name matches with the list of product names below:
                                ----------------------------
                                ----------------------------
                                ----------------------------
                                Products list:
                                2" PVC Wrapping Tape (Color | Green, Blue or Black)
                                Spray Paint (Color | Bright Gold, Grey27, Red, Dark Blue, Dark Green, Brown, Black, Chrome Silver, Lacquer Clear or Matte Black)
                                Duct Tape
                                Masking Tape
                                Asmaco GP Masking Tape
                                ----------------------------
                                ----------------------------
                                ----------------------------
                                Matching criteria:
                                1. The spellings MUST match
                                2. The characters may be in uppercase or lowercase
                                3. Some integer after the name is allowed
                                ----------------------------
                                ----------------------------
                                ----------------------------

                                YOU MUST STRICTLY FOLLOW THE RESPONSE FORMAT
                                ```json
                                {
                                    'products_list': The list of products whose name is incorrect. 
                                }
                                ```
                                DO NOT PROVIDE ANY OTHER DETAILS OR EXPLANATIONS IN ADDITION TO THE JSON CONTENT
                                EXAMPLE:
                                If the product names are 2" PVC Wrapping Tape Black, Lagune (Blue)18, and Chrome Silver, then the output should be
                                ```json
                                {
                                    'products_list': '
                                        * Lagune (Blue)18 needs to be changed to Spray Paint Dark Blue 
                                        * Chrome Silver needs to be changed to Spray Paint Chrome Silver'
                                } 
                                """
                },
                {
                    "type": "text",
                    "text": """
                            ```json
                                {
                                "bill_id": "02620",
                                "distributor_name": "GREEN CIRCLE TRADING CO LLC",
                                "products": ["2\" PVC wrapping Tape", "Spray Paint Brown 26", "Spray Paint Black 02", "Chrome Silver", "Lagune (Blue) 18", "Matt Black 20"],
                                "each_product_prize": [
                                    {
                                    "product_name": "2\" PVC wrapping Tape",
                                    "quantity": 3,
                                    "unit_price": 0.94,
                                    "total_price": 2.82
                                    },
                                    {
                                    "product_name": "Spray Paint Brown 26",
                                    "quantity": 5,
                                    "unit_price": 3.33,
                                    "total_price": 16.65
                                    },
                                    {
                                    "product_name": "Spray Paint Black 02",
                                    "quantity": 5,
                                    "unit_price": 3.33,
                                    "total_price": 16.65
                                    },
                                    {
                                    "product_name": "Chrome Silver",
                                    "quantity": 5,
                                    "unit_price": 3.50,
                                    "total_price": 17.50
                                    },
                                    {
                                    "product_name": "Lagune (Blue) 18",
                                    "quantity": 3,
                                    "unit_price": 3.33,
                                    "total_price": 9.99
                                    },
                                    {
                                    "product_name": "Matt Black 20",
                                    "quantity": 3,
                                    "unit_price": 3.33,
                                    "total_price": 9.99
                                    }
                                ],
                                "total_cost": "73.60"
                                }
                                ```
                            """
                }
            ],
        }
    ],
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    # model="meta-llama/llama-4-maverick-17b-128e-instruct",
)

print(chat_completion.choices[0].message.content)

