import streamlit as st
import transformers
import torch
from langchain import HuggingFacePipeline, PromptTemplate, LLMChain

# Load model and tokenizer
model = "ELeutherAI/gpt-neo-125m"
tokenizer = transformers.AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id
)

# Initialize Langchain LLM
llm = HuggingFacePipeline(pipeline=pipeline)
prompt = PromptTemplate(input_variables=["content"], template="Tell me a story about {content}.")
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("Story Generator")
st.write("Enter a topic to generate a story.")

# User input
user_input = st.text_input("Enter a topic:", "aliens")

if st.button("Generate Story"):
    with st.spinner("Generating..."):
        story = chain.run(user_input)
        st.write("### Generated Story:")
        st.write(story)
