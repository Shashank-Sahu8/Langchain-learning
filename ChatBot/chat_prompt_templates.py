from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

chat_template=ChatPromptTemplate([
    ("system","You are a helpful {domain} expert"),
     ("human","Provide detailed information about {topic}.")
],     input_variables=["domain","topic"]
)
prompt=chat_template.invoke({'domain':'medical','topic':'diabetes'})

print(prompt) 