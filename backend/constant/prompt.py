prompt = """
Extract data from invoice/LPO images and return ONLY valid JSON in this exact format:
json
{
  "lpo_no": "string",
  "date": "DD/MM/YYYY",
  "distributor_name": "string",
  "each_product_prize": [
    {
      "product_name": "string",
      "quantity": "string",
      "unit_price": "string",
      "total_price": "string"
    }
  ]
}
CRITICAL RULES:

Output ONLY JSON - no text, explanations, or backticks
LPO number: Extract exact number (e.g., "07796", "9339")
Date: Use DD/MM/YYYY format from document
Distributor name: Extract SUPPLIER/VENDOR name only (NOT the buyer/customer). The list of Distributor Names is as follows:
    - ABU DHABI ARCH FOR BUILDING MATERIALS
    - AL MILAD HARDWARE TRADING 
    - BETTER CHOICE GENERAL TRADING LLC
    - CATCO STAR TRADING LLC
    - GREEN CIRCLE TRADING CO. LLC
    - MOHAMMED AL KITBI GEN. TRADING LLC
    - MASOUD AL JUNAIDI BUILDING MATERIAL TRADING LLC
    - M.H.A.H. TRADING CO. LLC
    - SAFELAND TRADING LLC
    - TRENT INTERNATIONAL GEN. TRDG (M.D.)
    - WEST CITY AUTO SPARE PARTS LLC
**CRITICAL:** Anchor Allied Trading Company LLC IS NOT a Distributor name. 
Products: Include ALL line items with available pricing data
If any field is missing, use empty string ""
For quantity/prices: preserve original format including units (e.g., "10 ctn", "44/-")

DO NOT include buyer names like "Anchor Allied" - only extract the supplier/vendor company name.
"""