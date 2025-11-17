from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import DirectoryLoader,PyMuPDFLoader
# load_dotenv()

# mode=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# parser=StrOutputParser()

loader=DirectoryLoader(
    path=r'C:\Users\jeeva\OneDrive\Desktop\LangChainP\DocLoaders\directory_loader_demo_data',
    glob='*.pdf',
    loader_cls=PyMuPDFLoader
)
# docs=loader.load()
# print(docs[7].page_content)
# simple loading that takes time and also loads entire doc all togather in the memory that takes time and not good method
#but lazy_loading does diffrently provides genrator of doc and provides content or loads content in memory on demand that too not all at once rather the page demanded

docs=loader.lazy_load()

for docum in docs:
    print(docum.metadata)
    
    