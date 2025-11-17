from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="Write a joke about {topic} in 20 words.",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Translate the following joke into Hindi: {joke}",
    input_variables=["joke"]
)
parser=StrOutputParser()

chain=RunnableSequence(
    prompt1,
    prompt2,
    model,
    parser
)
result=chain.invoke({"topic":"computers"})

print(result)