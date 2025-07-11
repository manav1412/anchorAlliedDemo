import os
from PIL import Image, ImageEnhance

def method3_pil_enhancement(image_path):
    """PIL-based enhancement - good for brightness/contrast"""
    img = Image.open(image_path)
    
    # Convert to grayscale
    gray_img = img.convert('L')
    
    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(gray_img)
    contrast_enhanced = contrast_enhancer.enhance(1.5)
    
    # Enhance sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(contrast_enhanced)
    sharp_enhanced = sharpness_enhancer.enhance(2.0)
    
    return sharp_enhanced

image_path = "/home/neebal/Desktop/POC/anchor-allied/Sample_PO/green_circle.jpg"
last_slash_index = image_path.rfind('/')
image_name = image_path[last_slash_index:]
# Remove extension '.jpg', '.png', etc.
image_name = image_name[:-4]
output_dir="./Denoised_All_Samples"
os.makedirs(output_dir, exist_ok=True)
pil = method3_pil_enhancement(image_path)
pil.save(f"{output_dir}/{image_name}_method3_sharp.png")