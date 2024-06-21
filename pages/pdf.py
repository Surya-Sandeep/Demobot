import streamlit as st
from PyPDF2 import PdfReader
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

# Streamlit app
def main():
    st.title("Chat with PDF using LangChain and OpenAI")

    # Set your OpenAI API key
    openai_api_key = st.sidebar.text_input("OpenAI API Key", key="chatbot_api_key")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    # Upload PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.text_area("PDF Content", pdf_text, height=300)
        
        # Split the text for better processing with OpenAI
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        split_texts = text_splitter.split_text(pdf_text)
        
        # Create Document objects for each chunk
        documents = [Document(page_content=chunk) for chunk in split_texts]

        # Initialize the LangChain components with GPT-3.5 Turbo model
        try:
            llm = OpenAI(model_name="text-gpt-3.5-turbo", openai_api_key=openai_api_key)
            qa_chain = LLMChain(llm, chain_type="map_reduce")
        except Exception as e:
            st.error(f"Error initializing OpenAI: {e}")
            return

        # User question input
        question = st.text_input("Ask a question about the PDF content")
        
        if st.button("Get Answer"):
            if question:
                # Process each chunk and get answers
                answers = []
                for doc in documents:
                    try:
                        response = qa_chain.run(input_documents=[doc], question=question)
                        answers.append(response)
                    except Exception as e:
                        st.error(f"Error processing document: {e}")
                        answers.append("Error")

                # Combine answers and display the final answer
                final_answer = " ".join(answers)
                st.write("Answer:", final_answer)
            else:
                st.write("Please enter a question.")
                
if __name__ == "__main__":
    main()
