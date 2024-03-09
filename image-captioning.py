import warnings
from PIL import Image
from transformers import AutoProcessor
from transformers import BlipForConditionalGeneration
from transformers.utils import logging

logging.set_verbosity_error()

# Suppress warning message
warnings.filterwarnings("ignore", message="Using the model-agnostic default `max_length`")

# Load the Large Language Model (LLM)
model = BlipForConditionalGeneration.from_pretrained(
    "./blip-image-captioning-base")

# Load the processor
processor = AutoProcessor.from_pretrained(
    "./blip-image-captioning-base")

# Load the image
image = Image.open("./test_image.jpg")

# Create the input
inputs = processor(image, return_tensors="pt")

# Get the outupt
out = model.generate(**inputs)

# Print the output
print(processor.decode(out[0], skip_special_tokens=True))
