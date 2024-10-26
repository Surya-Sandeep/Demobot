import streamlit as st
import openai

# Set page title
st.set_page_config(
    page_title = "A Streamlit app powered by OpenAi",
    page_icon= "🦄"
)
# Set your OpenAI API key
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.sidebar.warning("Please enter your OpenAI API key to continue.")
else:
    openai.api_key = openai_api_key

# Function to generate blog content
def generate_blog(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes blog posts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    blog_content = response.choices[0].message['content'].strip()
    return blog_content

# Streamlit app
def main():
    st.title("AI Blog Generator")

    # User input for blog topic
    blog_topic = st.text_input("Enter the blog topic:")

    if st.button("Generate Blog"):
        if blog_topic:
            prompt = f"Write a detailed blog post about {blog_topic}."
            with st.spinner("Generating blog..."):
                blog_content = generate_blog(prompt)
            st.subheader("Generated Blog Post")
            st.write(blog_content)
        else:
            st.error("Please enter a blog topic to generate content.")

if __name__ == "__main__":
    main()
