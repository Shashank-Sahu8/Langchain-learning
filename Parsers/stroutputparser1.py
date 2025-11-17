from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.output_parsers import StrOutputParser

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template1=PromptTemplate(template="Provide a brief summary for the following text: {text}",input_variables=["text"])

template2=PromptTemplate(template="Write a 5 line poem about {topic}",input_variables=["topic"])

str_parser=StrOutputParser()

chain= template1 | model | str_parser | template2 | model |str_parser

result= chain.invoke({'text':"Shashank Sahu"})

print(result)