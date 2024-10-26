import os
import pandas as pd
import streamlit as st
import openai

# Streamlit sidebar for API key input
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.sidebar.warning("Please enter your OpenAI API key to continue.")
else:
    openai.api_key = openai_api_key

st.title(":page_facing_up: CSVbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("CSV Data:")
    st.write(df)

    def summarize_csv(df):
        # Summarize the CSV data
        summary = df.describe(include='all').to_string()
        return summary

    def query_csv(query, summary):
        # Custom function to query the CSV data
        prompt = f"Answer the following query based on the summarized CSV data:\n{query}\n\nCSV summary:\n{summary}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()

    summary = summarize_csv(df)

    user_query = st.text_input("Enter your query about the CSV data:")
    if user_query:
        response = query_csv(user_query, summary)
        st.write("Response:", response)
else:
    st.info("Please upload a CSV file to proceed.")
