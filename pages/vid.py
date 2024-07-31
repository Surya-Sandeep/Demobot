import streamlit as st
import cv2
import mediapipe as mp
import tempfile
import os

# Initialize MediaPipe face detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

st.title("Face Detection in Video")
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    st.video(tmp_file_path)

    # Process the video for face detection
    cap = cv2.VideoCapture(tmp_file_path)

    # Create a temporary directory to save processed frames
    processed_frames_dir = tempfile.mkdtemp()
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out_file_path = os.path.join(processed_frames_dir, 'processed_video.mp4')
    out = cv2.VideoWriter(out_file_path, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))

    with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Convert the BGR image to RGB.
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame and detect faces
            results = face_detection.process(rgb_frame)

            # Draw face detections
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)

            # Write the processed frame to the output file
            out.write(frame)

    cap.release()
    out.release()

    st.video(out_file_path)

    # Clean up temporary files
    os.remove(tmp_file_path)
    for file in os.listdir(processed_frames_dir):
        os.remove(os.path.join(processed_frames_dir, file))
    os.rmdir(processed_frames_dir)
