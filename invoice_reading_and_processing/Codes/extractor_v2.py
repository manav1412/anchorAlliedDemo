import cv2
import numpy as np
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    """Preprocess image to extract text regions"""
    # Read image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get binary image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Invert colors (text should be black on white background)
    binary = cv2.bitwise_not(binary)
    
    # Find contours to detect text regions
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by area and aspect ratio
    text_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        aspect_ratio = w / h
        
        # Filter based on size and aspect ratio
        if area > 500 and 0.1 < aspect_ratio < 20:
            text_regions.append((x, y, w, h))
    
    # Sort regions by y-coordinate (top to bottom)
    text_regions.sort(key=lambda region: region[1])
    
    return img, text_regions

def extract_text_from_regions(image_path, processor, model):
    """Extract text from each detected region"""
    img, regions = preprocess_image(image_path)
    extracted_texts = []
    
    for i, (x, y, w, h) in enumerate(regions):
        # Extract region from original image
        region = img[y:y+h, x:x+w]
        
        # Convert to PIL Image
        region_pil = Image.fromarray(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
        
        # Process with TrOCR
        try:
            pixel_values = processor(images=region_pil, return_tensors="pt").pixel_values
            generated_ids = model.generate(pixel_values)
            text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            
            if text.strip():  # Only add non-empty text
                extracted_texts.append(f"Region {i+1}: {text}")
                
        except Exception as e:
            print(f"Error processing region {i+1}: {e}")
    
    return extracted_texts

# Alternative approach: Use EasyOCR for better document handling
def extract_with_easyocr(image_path):
    """Alternative using EasyOCR which handles full documents better"""
    try:
        import easyocr
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image_path)
        
        extracted_text = []
        for (bbox, text, confidence) in results:
            if confidence > 0.5:  # Filter by confidence
                extracted_text.append(text)
        
        return '\n'.join(extracted_text)
    except ImportError:
        print("EasyOCR not installed. Install with: pip install easyocr")
        return None

# Main execution
def main():
    image_path = r'/home/neebal/Desktop/POC/anchor-allied/Sample PO/mhah.jpg'
    
    # Method 1: Try EasyOCR first (better for documents)
    print("Method 1: Using EasyOCR...")
    easyocr_result = extract_with_easyocr(image_path)
    if easyocr_result:
        with open('extracted_easyocr.txt', 'w') as f:
            f.write(easyocr_result)
        print("EasyOCR results saved to 'extracted_easyocr.txt'")
    
    # Method 2: Use TrOCR with preprocessing
    print("\nMethod 2: Using TrOCR with preprocessing...")
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
    
    trocr_results = extract_text_from_regions(image_path, processor, model)
    
    with open('extracted_trocr_regions.txt', 'w') as f:
        f.write('\n'.join(trocr_results))
    
    print("TrOCR results saved to 'extracted_trocr_regions.txt'")
    
    # Method 3: Focus on handwritten parts only
    print("\nMethod 3: Manual crop for handwritten sections...")
    # You'll need to manually identify handwritten regions
    # For your image, the handwritten parts appear to be in the "Mr/M/s" field and items
    
if __name__ == "__main__":
    main()