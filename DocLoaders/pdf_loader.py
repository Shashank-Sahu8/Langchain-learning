from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser=StrOutputParser()

loader=PyPDFLoader(r'C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\Resume Shashank Sahu.pdf')
doc=loader.load()


prompt=PromptTemplate(
    template="Is this person capable to get job in Google? /n {data} in 10 words.",
    input_variables=['data']
)

chain=prompt | model | parser

result=chain.invoke({"data":doc[0].page_content})

print(result)