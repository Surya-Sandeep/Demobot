import streamlit as st
from diffusers import DiffusionPipeline
import io
from PIL import Image

# Load the diffusion model pipeline
pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-3-medium")

# Streamlit application
st.title("Image Generator 🖼️")

# Input for image description
image_desc = st.text_input("Enter the description of the image:")

# Button to generate image
if st.button("Generate Image"):
    if image_desc:
        with st.spinner("Generating image..."):
            # Generate the image
            image = pipeline(prompt=image_desc).images[0]
            
            # Convert image to bytes for display and download
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_bytes = buffered.getvalue()
            
            # Display the image
            st.image(img_bytes, caption="Generated Image", use_column_width=True)

            # Download button
            st.download_button(
                label="Download Image",
                data=img_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.error("Please enter an image description.")
