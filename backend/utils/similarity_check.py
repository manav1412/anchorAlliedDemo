import pandas as pd
from sentence_transformers import SentenceTransformer, util
import os

# Construct the absolute path to the Excel file
file_path = os.path.join(os.path.dirname(__file__), '../data/Sku Dump.xlsx')

# Load Excel file if it exists
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    print("⚠️ Sku Dump.xlsx not found — skipping data load")
    df = None

# Load the transformer model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

def fetch_similar_item(input_word):
    if df is None:
        raise FileNotFoundError("Sku Dump.xlsx not found. Make sure it is bundled with your deployment.")

    if "Item_Desc" not in df.columns or "Item code" not in df.columns:
        raise ValueError("Required columns not found in Excel file. Ensure 'Item_Desc' and 'Item code' are present.")

    descriptions = df['Item_Desc'].astype(str).tolist()

    # Encode input and descriptions
    all_texts = [input_word] + descriptions
    embeddings = model.encode(all_texts, convert_to_tensor=True)

    # Compute similarity
    cosine_scores = util.cos_sim(embeddings[0], embeddings[1:])
    best_idx = cosine_scores.argmax().item()
    best_score = cosine_scores[0][best_idx].item()

    similar_item = df['Item_Desc'][best_idx]
    item_code = df['Item code'][best_idx]

    print("Best Match:", similar_item)
    print("Best item code:", item_code)
    print("Similarity Score:", round(best_score * 100, 2), "%")

    return similar_item, item_code
