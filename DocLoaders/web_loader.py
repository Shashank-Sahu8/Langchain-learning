from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

url="https://shashank-sahu.me"

loader=WebBaseLoader(url)

docs=loader.load()
prompt=PromptTemplate(
    template="Is this person technical expert?/n {details}",
    input_variables=["details"]
)

chain= prompt|model|parser

result=chain.invoke({"details":docs[0].page_content})

print(result);

# print(len(docs))
# print(docs[0].page_content)