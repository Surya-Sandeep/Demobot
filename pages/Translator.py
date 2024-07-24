import streamlit as st
from deep_translator import GoogleTranslator

# Dictionary to map language names to language codes
LANGUAGE_CODES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Hindi": "hi",
    "Arabic": "ar",
    "Bengali": "bn",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    # Add more languages as needed
}

# Set up the Streamlit app
st.title("🌐 Text Translator")

# Dropdown for source language
source_language = st.selectbox("Select source language:", list(LANGUAGE_CODES.keys()), index=0)

# Dropdown for target language
target_language = st.selectbox("Select target language:", list(LANGUAGE_CODES.keys()), index=1)

# Get input text from the user
text_to_translate = st.text_area("Enter text to translate:")

# Button to perform translation
if st.button("Translate"):
    if text_to_translate:
        source_lang_code = LANGUAGE_CODES[source_language]
        target_lang_code = LANGUAGE_CODES[target_language]
        
        # Check if source and target languages are different
        if source_lang_code != target_lang_code:
            try:
                # Initialize the translator with source and target languages
                translator = GoogleTranslator(source=source_lang_code, target=target_lang_code)
                translated_text = translator.translate(text_to_translate)
                
                # Display the translated text
                st.success(f"Translated Text: {translated_text}")
            except Exception as e:
                st.error(f"Translation Error: {e}")
        else:
            st.warning("Source and target languages must be different.")
    else:
        st.warning("Please enter text to translate.")

