from groq import Groq
import os

# TO DO: PARSING USING PROMPT
# CREATE INTERFACE

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def call_groq_notifier(groq_res):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
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

                                    The output shpuld look something like this example. in product_list mention which products needs to be updated into which product name in a string. 
                                    It must be a short descriptive string for eg:- "Spray paint black 32, Spray paint blue 54 needs to be changed to Spray paint black, Spray paint blue"
                                    There should ONLY be the JSON. No other explanations, at any cost.
                                    DANGER: If you give anything else in addition to JSON, there will be severe consequences.
                                
                                    ```json
                                    {
                                        "products_list": """
                                        """
                                    }
                                    ```
                                    """
                    },
                    {
                        "type": "text",
                        "text": groq_res
                    }
                ],
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        # model="meta-llama/llama-4-maverick-17b-128e-instruct",
    )
    return chat_completion.choices[0].message.content