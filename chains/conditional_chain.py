from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback"
    )
    
parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Classify the sentiment of the following text: {text}\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser2.get_format_instructions()} 
)

prompt2=PromptTemplate(
    template="Write an appropriate response to this positive in 50 words feedback: {text}",
    input_variables=[ "text"]
)

prompt3=PromptTemplate(
    template="Write an appropriate response to this negative in 50 words feedback: {text}",
    input_variables=["text"]
)

classification_chain= prompt1 | model | parser2

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive", prompt2 | model | parser),
    (lambda x:x.sentiment=="negative", prompt3 | model | parser),
    RunnableLambda(lambda _: "No sentiment detected.")
)
    
chain=classification_chain | branch_chain

result=chain.invoke({
    "text":"Its the worst experience Ive ever had with any company. The product broke within a week and customer service was unhelpful."
})

print(result)

chain.get_graph().print_ascii()