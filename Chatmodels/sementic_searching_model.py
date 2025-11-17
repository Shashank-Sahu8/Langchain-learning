from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents=[
    "LangChain is a framework for developing applications powered by language models.",
    "Shashank Sahu is a good boy.",
    "Hugging Face provides open-source libraries for machine learning.",
    "Semantic search improves search accuracy by understanding the intent and contextual meaning of terms."
    "Python is a popular programming language."
]

query="language hugging sahu langchain"

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

# both should be 2d list since doc_embedding is already 2d hence need to convert query_embedding to 2d
# similarities=cosine_similarity([query_embedding], doc_embeddings)
# similarities=cosine_similarity([query_embedding], doc_embeddings)[0]
similarities=cosine_similarity([query_embedding], doc_embeddings)[0]
# print(similarities)
index,score=sorted(list(enumerate(similarities)),key=lambda x:x[1],reverse=True)[0]

print(documents[index])

print(f"Similarity Score: {score}")