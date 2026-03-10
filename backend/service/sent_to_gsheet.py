import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

WEBHOOK_URL = os.getenv("GSHEET_WEBHOOK_URL")
print("WEBHOOK URL",WEBHOOK_URL)

def send_to_google_sheets(document):
    data = {
        "lpo_no": document.get("lpo_no"),
        "customer_name": document.get('distributor_name'),
        "item_code": document.get('item_code'),
        "item_description": json.dumps(document.get("each_product_prize")),
        "date": document.get("date")
    }
    
    print("Data sent to CSV:", data)
    response = requests.post(WEBHOOK_URL, json=data)
    print("Sent to Google Sheets:", response.text)