import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
from skimage import restoration, filters, exposure
from scipy import ndimage

def method1_opencv_basic(image_path):
    """Basic OpenCV denoising - good for general noise"""
    # Load image
    img = cv2.imread(image_path)
    
    # Convert to grayscale for better text processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Non-local Means Denoising
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
    
    # Optional: Apply Gaussian blur to smooth further
    smoothed = cv2.GaussianBlur(denoised, (3, 3), 0)
    
    return denoised, smoothed

def method2_opencv_advanced(image_path):
    """Advanced OpenCV with morphological operations"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Denoising
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
    
    # 2. Enhance contrast using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)
    
    # 3. Sharpen the image
    kernel = np.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(enhanced, -1, kernel)
    
    # 4. Morphological operations to clean up
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    cleaned = cv2.morphologyEx(sharpened, cv2.MORPH_CLOSE, kernel)
    
    return enhanced, sharpened, cleaned

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
    
    # Apply unsharp mask filter
    unsharp = sharp_enhanced.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    return contrast_enhanced, sharp_enhanced, unsharp

def method4_scikit_image(image_path):
    """Scikit-image based denoising - more advanced algorithms"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Normalize to 0-1 range
    normalized = gray.astype(np.float64) / 255.0
    
    # Apply different denoising methods
    # 1. Total Variation denoising
    tv_denoised = restoration.denoise_tv_chambolle(normalized, weight=0.1)
    
    # 2. Bilateral filter
    bilateral = restoration.denoise_bilateral(normalized, sigma_color=0.1, sigma_spatial=15)
    
    # 3. Non-local means
    nl_means = restoration.denoise_nl_means(normalized, patch_size=5, patch_distance=3, h=0.1)
    
    # Convert back to 0-255 range
    tv_result = (tv_denoised * 255).astype(np.uint8)
    bilateral_result = (bilateral * 255).astype(np.uint8)
    nl_result = (nl_means * 255).astype(np.uint8)
    
    return tv_result, bilateral_result, nl_result

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
    
    # 5. Final contrast adjustment
    contrast_adjusted = cv2.convertScaleAbs(unsharp, alpha=1.2, beta=10)
    
    return equalized, denoised, unsharp, contrast_adjusted

def compare_methods(image_path, output_dir="./Denoised_Green_Circle/"):
    """Compare all methods and save results"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Original image
    original = cv2.imread(image_path)
    original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    
    print("Processing with different methods...")
    
    # Method 1: Basic OpenCV
    basic1, basic2 = method1_opencv_basic(image_path)
    cv2.imwrite(f"{output_dir}method1_basic.png", basic1)
    cv2.imwrite(f"{output_dir}method1_smoothed.png", basic2)
    
    # Method 2: Advanced OpenCV
    adv1, adv2, adv3 = method2_opencv_advanced(image_path)
    cv2.imwrite(f"{output_dir}method2_enhanced.png", adv1)
    cv2.imwrite(f"{output_dir}method2_sharpened.png", adv2)
    cv2.imwrite(f"{output_dir}method2_cleaned.png", adv3)
    
    # Method 3: PIL
    pil1, pil2, pil3 = method3_pil_enhancement(image_path)
    pil1.save(f"{output_dir}method3_contrast.png")
    pil2.save(f"{output_dir}method3_sharp.png")
    pil3.save(f"{output_dir}method3_unsharp.png")
    
    # Method 4: Scikit-image
    ski1, ski2, ski3 = method4_scikit_image(image_path)
    cv2.imwrite(f"{output_dir}method4_tv.png", ski1)
    cv2.imwrite(f"{output_dir}method4_bilateral.png", ski2)
    cv2.imwrite(f"{output_dir}method4_nlmeans.png", ski3)
    
    # Method 5: Document-specific
    doc1, doc2, doc3, doc4 = method5_document_specific(image_path)
    cv2.imwrite(f"{output_dir}method5_equalized.png", doc1)
    cv2.imwrite(f"{output_dir}method5_denoised.png", doc2)
    cv2.imwrite(f"{output_dir}method5_unsharp.png", doc3)
    cv2.imwrite(f"{output_dir}method5_final.png", doc4)
    
    print(f"All results saved to {output_dir}")
    
    # Create comparison plot
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    images = [
        (original_gray, 'Original'),
        (basic1, 'OpenCV Basic'),
        (adv3, 'OpenCV Advanced'),
        (np.array(pil3), 'PIL Enhanced'),
        (ski2, 'Scikit Bilateral'),
        (doc4, 'Document Optimized')
    ]
    
    for i, (img, title) in enumerate(images):
        row, col = i // 3, i % 3
        axes[row, col].imshow(img, cmap='gray')
        axes[row, col].set_title(title)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}comparison.png", dpi=300, bbox_inches='tight')
    plt.show()

# Quick single method for best results on documents
def quick_document_denoise(image_path, output_path=None):
    """Quick and effective denoising for document images"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply the most effective combination for documents
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    equalized = clahe.apply(gray)
    
    denoised = cv2.fastNlMeansDenoising(equalized, None, 10, 7, 21)
    
    # Unsharp masking
    gaussian = cv2.GaussianBlur(denoised, (0, 0), 2.0)
    unsharp = cv2.addWeighted(denoised, 1.5, gaussian, -0.5, 0)
    
    result = cv2.convertScaleAbs(unsharp, alpha=1.2, beta=10)
    
    if output_path:
        cv2.imwrite(output_path, result)
        print(f"Denoised image saved to {output_path}")
    
    return result

# Usage example:
if __name__ == "__main__":
    # Replace with your image path
    image_path = "/home/neebal/Desktop/POC/anchor-allied/Sample_PO/green_circle.jpg"
    
    # Quick method - recommended for documents
    result = quick_document_denoise(image_path, "denoised_invoice.png")
    
    # Or compare all methods
    compare_methods(image_path)