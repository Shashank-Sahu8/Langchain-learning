from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

url="https://shashank-sahu.me"

loader=WebBaseLoader(url)

loaded_result=loader.load()

prompt=PromptTemplate(
    template="Make a doc obout the person in 200 words./n {details}",
    input_variables=["details"]
)

chain=prompt|model|parser

result=chain.invoke({"details":loaded_result[0].page_content})

splitter=CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5,
    separator="\n"
)

ans=splitter.split_text(result)

for answer in ans:
    print(answer)
    print("----")