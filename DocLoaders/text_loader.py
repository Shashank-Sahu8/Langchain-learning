from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write Summary of the following poem- \n {poem} in less than 30 words",
    input_variables=['poem']
)

loader = TextLoader(r'C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\cricket.txt', encoding='utf-8')

docs=loader.load()

chain=prompt | model |parser

result=chain.invoke({"poem":docs[0].page_content})

print(result)
