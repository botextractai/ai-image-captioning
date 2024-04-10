# Image captioning with a locally stored Large Language Model (LLM)

This example generates a caption of an image.

It runs fully local on your computer and it does not require a Graphics Processing Unit (GPU).

It uses the Salesforce [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://huggingface.co/Salesforce/blip-image-captioning-base) Large Language Model (LLM) and Hugging Face Transformers. Please note that is a very small model and its capabilities are therefore limited, but the results are still very impressive for its size.

This example uses this test image:

![alt text](https://github.com/botextractai/ai-image-captioning/blob/main/test_image.jpg "Test image")

to automatically generate this image caption:

`a set of toy cars and traffic cones`
