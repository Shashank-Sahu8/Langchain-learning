from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=PromptTemplate(
    template="Write a {paper_type} on the topic of {topic} with a lengthof {length} words.",
    input_variables=["paper_type", "topic", "length"]
)

parser=StrOutputParser()

chain= prompt | model | parser

result= chain.invoke({
    "paper_type":"Research Paper",
    "topic":"Artificial Intelligence",
    "length":500
})

print(result)
 
chain.get_graph().print_ascii()
