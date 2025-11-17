from langchain_google_genai import ChatGoogleGenerativeAI        
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_core.prompts import PromptTemplate
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

paper_input = st.selectbox("Select the type of paper:", ["Research Paper", "Review Paper", "Case Study", "White Paper"])

topic_input = st.text_input("Enter the topic of the paper:")

length_input = st.slider("Select the length of the paper (in words):", min_value=50, max_value=1000, step=50)

template=PromptTemplate(
    template="""Write a {paper_type} on the topic of {topic} with a length of {length} words.""",
    input_variables=["paper_type", "topic", "length"]
)

prompt=template.invoke(
    {
        "paper_type": paper_input,
        "topic": topic_input,
        "length": length_input
    }
)

if st.button("Answer"):
    response=model.invoke(prompt)
    st.write(response.content)