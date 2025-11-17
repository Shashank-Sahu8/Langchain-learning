from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_core.documents import Document

doc1=Document(page_content="Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions), and self-correction.",metadata={"source":"wiki1"})
doc2=Document(page_content="Machine learning (ML) is a subset of artificial intelligence (AI) that focuses on the development of algorithms and statistical models that enable computers to perform specific tasks without explicit instructions, relying instead on patterns and inference.",metadata={"source":"wiki2"})
doc3=Document(page_content="Deep learning is a subset of machine learning in artificial intelligence (AI) that has networks capable of learning from data that is unstructured or unlabeled. Also known as deep neural learning or deep neural network.",metadata={"source":"wiki3"})
doc4=Document(page_content="Natural language processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and generate human languages in a way that is valuable.",metadata={"source":"wiki4"})
doc5=Document(page_content="Computer vision is an interdisciplinary scientific field that deals with how computers can be made to gain high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that the human visual system can do.",metadata={"source":"wiki5"})
 
docs=[doc1,doc2,doc3,doc4,doc5]

vectorstore=Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"),
    collection_name="AI_Articles",
    persist_directory="./chroma_db"
)
    
# vectorstore.add_documents(docs)

# vectorstore.add_documents(docs)

# print(vectorstore.get(include=['embeddings','documents','metadatas']))


# print(vectorstore.similarity_search("Explain about Natural Language Processing?",k=2))

# print(vectorstore.similarity_search_with_score("Explain about Natural Language Processing?",k=2))

vectorstore.similarity_search_with_score(query="",filter={"source":"wiki4"})