from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# load image from the IAM database
image_path = r'/home/neebal/Desktop/POC/anchor-allied/Sample PO/mhah.jpg'
image = Image.open(image_path).convert("RGB")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

with open('extracted.txt', 'w') as f:
    f.write(generated_text)