import streamlit as st
import requests
from diffusers import DiffusionPipeline
import io
from PIL import Image

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
# Load the diffusion model pipeline
pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-3-medium")

# Streamlit application
st.title("Image Generator 🖼️")
@@ -21,15 +16,21 @@ def query(payload):
if st.button("Generate Image"):
    if image_desc:
        with st.spinner("Generating image..."):
            image_bytes = query({"inputs": image_desc})
            # Generate the image
            image = pipeline(prompt=image_desc).images[0]

            # Convert image to bytes for display and download
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_bytes = buffered.getvalue()

            # Display the image directly
            st.image(image_bytes, caption="Generated Image", use_column_width=True)
            # Display the image
            st.image(img_bytes, caption="Generated Image", use_column_width=True)

            # Download button
            st.download_button(
                label="Download Image",
                data=image_bytes,
                data=img_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
