from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class review(BaseModel):
    key_theme=Field(description="The key themes discussed in the review")
    summary=Field(description="A brief summary of the review")
    sentiment=Field(description="The sentiment of the review")
    pros=Field(default=None, description="List of pros mentioned in the review")
    cons=Field(default=None, description="List of cons mentioned in the review")
    name=Field(description="Name of the reviewer")
    
structured_model=model.with_structured_output(review)



result=structured_model.invoke("The laptop is great, but the processor is slightly weak if I try playing games. but the battery life is excellent.");

print(result)

 