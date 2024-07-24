import streamlit as st
import requests
import io
from PIL import Image

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit application
st.title("Image Generator 🖼️")

# Input for image description
image_desc = st.text_input("Enter the description of the image:")

# Button to generate image
if st.button("Generate Image"):
    if image_desc:
        with st.spinner("Generating image..."):
            image_bytes = query({"inputs": image_desc})
            # Open and display the image
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)

            # Convert image to bytes for download
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = buffered.getvalue()

            # Download button
            st.download_button(
                label="Download Image",
                data=img_str,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.error("Please enter an image description.")
