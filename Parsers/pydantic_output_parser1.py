from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from pydantic import Field,BaseModel
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Person(BaseModel):
    name:str= Field(description="Name of the fictional person")
    age: int=Field(gt=18,description="Age of the fictional person")
    city:str= Field(description="City of the fictional person")
    
parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Give me name, age and city of a fictional person \n {format_instructions}',
    input_variables=[],
    partial_variables={"format_instructions":parser.get_format_instructions()}   
)

prompt=template.format()

chain= template | model | parser

result= chain.invoke({})
print(result)