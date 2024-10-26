import streamlit as st
from parrot import Parrot
import torch
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Initialize the Parrot model (make sure to do this only once)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# Streamlit application
def main():
    st.title("Telugu News Paraphraser")
    
    # Input field for the phrase
    phrase = st.text_input("Enter a phrase to paraphrase:", "")
    
    if st.button("Generate Paraphrases"):
        if phrase:
            # Generate paraphrases
            para_phrases = parrot.augment(input_phrase=phrase, 
                                           diversity_ranker="levenshtein",
                                           do_diverse=True, 
                                           max_return_phrases=10, 
                                           max_length=32, 
                                           adequacy_threshold=0.2, 
                                           fluency_threshold=0.30)
            
            # Display paraphrases
            st.subheader("Generated Paraphrases:")
            for para_phrase in para_phrases:
                st.write(para_phrase)
        else:
            st.warning("Please enter a phrase before generating paraphrases.")

if __name__ == "__main__":
    main()
