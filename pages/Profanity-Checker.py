import streamlit as st
from better_profanity import profanity

# Set up the profanity filter
profanity.load_censor_words()

# Custom list of bad words
custom_bad_words = ["customword1", "customword2", "customword3"]

# Add custom bad words to the profanity filter
profanity.add_censor_words(custom_bad_words)

# Title of the Streamlit app
st.title("Profanity Checker and Censor")

# Text input from the user
text = st.text_area("Enter text to be checked and censored:", "")

# Check for inappropriate words
contains_profanity = profanity.contains_profanity(text)

# Display a message based on the presence of inappropriate words
if contains_profanity:
    st.warning("Warning: Inappropriate words were found. Please edit your text.")
    post_button_disabled = True
else:
    #st.success("No inappropriate words found.")
    post_button_disabled = False

# Check and censor the text if the button is enabled
if st.button("Post Comment", disabled=post_button_disabled):
    censored_text = profanity.censor(text)
    st.write("Comment:")
    st.write(censored_text)
