import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Load the model
model_id = "dreamlike-art/dreamlike-diffusion-1.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)
pipe = pipe.to("cuda")

# Streamlit app layout
st.title("Stable Diffusion Image Generator")

# User input for the prompt
prompt = st.text_area("Enter your prompt here:", "dreamlikeart, a grungy woman with rainbow hair, travelling between dimensions, dynamic pose, happy, soft eyes and narrow chin, extreme bokeh, dainty figure, long hair straight down, torn kawaii shirt and baggy jeans")

# Button to generate image
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            # Generate image
            image = pipe(prompt).images[0]
            
            # Convert the image to a format suitable for Streamlit
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.imshow(image)
            ax.axis('off')
            
            # Save the figure to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format="png", bbox_inches='tight', pad_inches=0)
            buf.seek(0)
            
            # Display image in Streamlit
            st.image(buf, use_column_width=True)
    else:
        st.warning("Please enter a prompt.")
