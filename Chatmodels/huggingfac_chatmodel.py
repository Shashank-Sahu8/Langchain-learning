from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task='text-generation',
)
 
model = ChatHuggingFace(llm=llm)

result=model.invoke("Hello, my name is")

print(result.content)