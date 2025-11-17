from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="genrate a joke about {topic} in less than 50 words.",
    input_variables=["topic"]     
)

prompt2=PromptTemplate(
    template="explain the following joke in detail: {joke} in 50 words.",
    input_variables=["joke"]
)

passthrough=RunnablePassthrough()

joke_gen_chain=RunnableSequence(
    prompt1,
    model,
    parser
)

parallel_chain=RunnableParallel(
    {   
        'joke':RunnableSequence(prompt2, model, parser),
        'passthrough':RunnablePassthrough()
    }
)

chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)
result=chain.invoke({"topic":"technology"})
print(result)
