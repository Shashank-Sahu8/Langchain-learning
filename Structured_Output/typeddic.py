from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict,Annotated,Optional

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class review(TypedDict):
    key_themes: Annotated[list[str], "The key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]

structured_model=model.with_structured_output(review)

result=structured_model.invoke("The laptop is great, but the processor is slightly weak if I try playing games. but the battery life is excellent.");

print(result)

