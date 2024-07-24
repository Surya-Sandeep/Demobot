import streamlit as st
import requests
import io

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
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
            
            # Display the image directly
            st.image(image_bytes, caption="Generated Image", use_column_width=True)

            # Download button
            st.download_button(
                label="Download Image",
                data=image_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.error("Please enter an image description.")
