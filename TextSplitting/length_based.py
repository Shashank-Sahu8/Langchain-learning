from langchain_text_splitters import CharacterTextSplitter

text=r"""
(venv) PS C:\Users\jeeva\OneDrive\Desktop\LangChainP> python DocLoaders/pdf_loader.py
  File "C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\pdf_loader.py", line 13
    loader=PyPDFLoader('C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\Resume Shashank Sahu.pdf')
                                                                 
                                      ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
(venv) PS C:\Users\jeeva\OneDrive\Desktop\LangChainP> 



from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser=StrOutputParser()

loader=PyPDFLoader('C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\Resume Shashank Sahu.pdf')
doc=loader.load()

print(docs[0])
"""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator="\n"
)

result=splitter.split_text(text)

print(len(result))
