import streamlit as st
import requests
import io
from PIL import Image

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit application
st.title("Image Generator 🖼️")

# Display category links
st.markdown("""
**Explore AI Image Prompts:**
- [AI Image Prompts for Marketing Materials](https://narrato.io/blog/40-ai-image-prompts-to-create-amazing-visuals-effortlessly/#place3)
- [AI Image Prompts for Photography](https://narrato.io/blog/40-ai-image-prompts-to-create-amazing-visuals-effortlessly/#place4)
- [AI Image Prompts for Art](https://narrato.io/blog/40-ai-image-prompts-to-create-amazing-visuals-effortlessly/#place5)
- [AI Image Prompts for Cartoons and Caricatures](https://narrato.io/blog/40-ai-image-prompts-to-create-amazing-visuals-effortlessly/#place6)
- [AI Image Prompts for Video Game Design](https://narrato.io/blog/40-ai-image-prompts-to-create-amazing-visuals-effortlessly/#place7)
""")

# Input for image description
image_desc = st.text_area("Enter the description of the image:", height=150)

# Button to generate image
if st.button("Generate Image"):
    if image_desc:
        with st.spinner("Generating image..."):
            image_bytes = query({"inputs": image_desc})
            
            try:
                # Open image using PIL and convert to high-resolution format
                image = Image.open(io.BytesIO(image_bytes))
                image = image.convert("RGB")
                
                # Display the image directly from bytes
                st.image(image_bytes, caption="Generated Image", use_column_width=True)

                # Convert image to JPEG format
                buffered = io.BytesIO(image_bytes)
                img_str = buffered.getvalue()

                # Download button
                st.download_button(
                    label="Download Image",
                    data=img_str,
                    file_name="generated_image.jpg",
                    mime="image/jpeg"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter an image description.")
