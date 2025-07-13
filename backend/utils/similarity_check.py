import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load your Excel file
df = pd.read_excel("/home/neebal/Desktop/similarity_mapping/Sku Dump.xlsx")

def fetch_similar_item(input_word):
    # Make sure the column exists
    if "Item_Desc" not in df.columns:
        raise ValueError("Column 'Item_Desc' not found in Excel file.")

    # Convert descriptions to list
    descriptions = df['Item_Desc'].astype(str).tolist()

    # Load pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight & fast

    # Generate embeddings
    all_texts = [input_word] + descriptions
    embeddings = model.encode(all_texts, convert_to_tensor=True)

    # Compute cosine similarities
    cosine_scores = util.cos_sim(embeddings[0], embeddings[1:])

    # Find best match index
    best_idx = cosine_scores.argmax().item()
    best_score = cosine_scores[0][best_idx].item()

    # Print result
    print("Best Match:", df['Item_Desc'][best_idx])
    print("Best item code:", df['Item code'][best_idx])
    print("Similarity Score:", round(best_score * 100, 2), "%")
    
    similar_item = df['Item_Desc'][best_idx]
    item_code = df['Item code'][best_idx]
    
    return similar_item, item_code

