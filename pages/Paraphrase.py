import streamlit as st
from transformers import pipeline

# Load the paraphrasing model
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def paraphrase_text(text):
    # Paraphrase the input text
    paraphrased = paraphraser(text, max_length=150, num_return_sequences=1)
    return paraphrased[0]['generated_text']

# Streamlit app
st.title("Text Paraphraser")

# Text input
input_text = st.text_area("Enter the text you want to paraphrase:", height=200)

# Button to trigger paraphrasing
if st.button("Paraphrase"):
    if input_text:
        with st.spinner("Paraphrasing..."):
            paraphrased_output = paraphrase_text(input_text)
        st.success("Paraphrased Text:")
        st.write(paraphrased_output)
    else:
        st.error("Please enter some text to paraphrase.")
