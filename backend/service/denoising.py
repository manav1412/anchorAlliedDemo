import base64
import io
from PIL import Image, ImageEnhance

def method3_pil_enhancement_from_base64(image_base64: str) -> str:
    """Enhance image from base64 input and return base64 of enhanced image."""

    # Decode base64 to bytes
    image_bytes = base64.b64decode(image_base64)
    image_stream = io.BytesIO(image_bytes)

    # Open image
    img = Image.open(image_stream)

    # Convert to grayscale
    gray_img = img.convert('L')

    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(gray_img)
    contrast_enhanced = contrast_enhancer.enhance(1.5)

    # Enhance sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(contrast_enhanced)
    sharp_enhanced = sharpness_enhancer.enhance(2.0)

    # Save to in-memory buffer
    buffered = io.BytesIO()
    sharp_enhanced.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return img_base64
