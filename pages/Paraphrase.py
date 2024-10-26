import streamlit as st
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

# Load the Pegasus model and tokenizer
model_name = "google/pegasus-large"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Function to generate paraphrases
def generate_paraphrases(input_text):
    # Prepare the input for the model
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate paraphrases
    with torch.no_grad():
        output_ids = model.generate(input_ids, num_beams=5, num_return_sequences=5, max_length=60, early_stopping=True)

    # Decode the generated paraphrases
    paraphrases = [tokenizer.decode(output_id, skip_special_tokens=True) for output_id in output_ids]
    return paraphrases

# Streamlit application
def main():
    st.title("Paraphrasing Application")
    
    # Input field for the phrase
    phrase = st.text_input("Enter a phrase to paraphrase:", "")
    
    if st.button("Generate Paraphrases"):
        if phrase:
            # Generate paraphrases
            para_phrases = generate_paraphrases(phrase)
            
            # Display paraphrases
            st.subheader("Generated Paraphrases:")
            for para_phrase in para_phrases:
                st.write(para_phrase)
        else:
            st.warning("Please enter a phrase before generating paraphrases.")

if __name__ == "__main__":
    main()
