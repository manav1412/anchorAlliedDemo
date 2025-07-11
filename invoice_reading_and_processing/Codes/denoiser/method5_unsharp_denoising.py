import cv2
import os

def method5_document_specific(image_path):
    """Specialized for document images like invoices"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Adaptive histogram equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    equalized = clahe.apply(gray)
    
    # 2. Denoising
    denoised = cv2.fastNlMeansDenoising(equalized, None, 10, 7, 21)
    
    # 3. Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(denoised, (3, 3), 0)
    
    # 4. Unsharp masking for text clarity
    gaussian = cv2.GaussianBlur(blurred, (0, 0), 2.0)
    unsharp = cv2.addWeighted(blurred, 1.5, gaussian, -0.5, 0)
    
    return unsharp

image_path = "/home/neebal/Desktop/POC/anchor-allied/Sample_PO/green_circle.jpg"
last_slash_index = image_path.rfind('/')
image_name = image_path[last_slash_index:]
# Remove extension '.jpg', '.png', etc.
image_name = image_name[:-4]
output_dir="./Denoised_All_Samples"
os.makedirs(output_dir, exist_ok=True)
doc = method5_document_specific(image_path)
cv2.imwrite(f"{output_dir}/{image_name}_method5_unsharp.png", doc)