from langchain_huggingface import HuggingFacePipeline
import os

os.environ['HF_HOME']='D:/huggingface_cache'

llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.7,
        max_new_tokens=256,
    )
)

# model=ChatHuggingFace(llm=llm)
result=llm.invoke("Who is Shashank Sahu")
print(result)