import streamlit as st
from nudenet import NudeDetector
from PIL import Image
import tempfile

# Set up the NudeDetector
nude_detector = NudeDetector()

# Title of the Streamlit app
st.title("Explicit Content Detection")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file, format='JPEG')
        temp_file_path = temp_file.name
    
    # Detect nudity
    detections = nude_detector.detect(temp_file_path)
    
    # Display a message based on the presence of inappropriate content
    explicit_content_detected = False
    for detection in detections:
        label = detection.get('class', 'class')
        score = detection.get('score', 'score')
        box = detection.get('box', 'box')
        #st.write(f"Label: {label}, Score: {score}, Box: {box}")
        if label in ["FEMALE_BREAST_EXPOSED", "FEMALE_GENITALIA_EXPOSED", "MALE_GENITALIA_EXPOSED","BUTTOCKS_EXPOSED"]: 
            explicit_content_detected = True

    if explicit_content_detected:
        st.warning("Explicit content detected. Upload disabled.")
        post_button_disabled = True
    else:
        post_button_disabled = False
    
    # Check and censor the text if the button is enabled
    if st.button("Post Image", disabled=post_button_disabled):
        st.image(image, caption='Uploaded Image', use_column_width=True)
