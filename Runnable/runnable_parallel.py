from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Genrate a tweet about {topic} in less than 50 words.",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Genrate a LinkedIn post about {topic} in less than 100 words.",
    input_variables=["topic"]
)

chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1, model, parser),
        'linkedin_post':RunnableSequence(prompt2, model, parser)
    }
)   
result=chain.invoke({"topic":"Renewable Energy"})

print(result)

chain.get_graph().print_ascii()