prompt = """
Extract data from invoice/LPO images and return ONLY valid JSON in this exact format:
json
{
  "lpo_no": "string",
  "date": "DD/MM/YYYY",     (make the date in this format only, if only the last 2 digits of year is found add 20 in the begin that makes the YYYY complete)
  "distributor_name": "string",
  "each_product_prize": [
    {
      "product_name": "string",     (handle the ditto mark, When you see quotation marks (""), ditto marks (″), or the word "ditto" in product descriptions, these indicate repetition of text from the previous line(s) The ditto marks mean "same as above" for the preceding words   You must reconstruct the full product name by combining the repeated text with the new text)
      "quantity": "string",     (Don't include any unit just the number)
      "unit_price": "string",    (Don't include any unit just the number)
      "total_price": "string"    (calculate total prize by adding all quantity*unit_price if not present)
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

It is each_product_prize and NOT each_product_price in the JSON.
"""