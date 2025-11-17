from langchain_community.vectorstores import Chroma,FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
load_dotenv()

embeddings=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

parser=StrOutputParser()

# model=GoogleGenerativeAIEmbeddings(model="gemini-2.5-flash")

documtnts=[
     Document(page_content="India is a developing country with a population of over 1.3 billion people. Despite significant economic growth in recent years, a large portion of the population still lives below the poverty line. The government has implemented various schemes and programs to alleviate poverty, but challenges such as unemployment, lack of education, and inadequate healthcare continue to persist."),
     Document(page_content="Poverty in India is a multifaceted issue that requires a comprehensive approach. Economic development, social welfare programs, and community-driven initiatives are all essential components in the fight against poverty. Additionally, addressing systemic issues such as corruption and inequality is crucial for creating sustainable change."),
     Document(page_content="Efforts to reduce poverty in India have seen some success, with millions of people lifted out of poverty over the past few decades. However, the COVID-19 pandemic has reversed some of these gains, pushing many back into poverty. Continued focus on inclusive growth and targeted interventions will be necessary to ensure long-term progress."),
     Document(page_content="Education plays a vital role in breaking the cycle of poverty in India. Access to quality education can empower individuals and communities, providing them with the skills and knowledge needed to improve their economic prospects. Government initiatives such as the Right to Education Act aim to ensure that all children have access to free and compulsory education."),
     Document(page_content="Healthcare is another critical area in the fight against poverty in India. Poor health outcomes can trap individuals and families in poverty, as they are unable to work or afford medical care. Strengthening healthcare infrastructure and ensuring access to affordable healthcare services are essential steps in addressing this issue.")
]

vectorstore=FAISS.from_documents(documtnts,embeddings)  
retriever=vectorstore.as_retriever(search_type="mmr",search_kwargs={"k":3,"lambda":0})
query="Write a detailed report on Poverty level in India"

result=retriever.invoke(query)

for i,doc in enumerate(result):
    
    print(f"Document {i+1}:\n{doc.page_content}\n")