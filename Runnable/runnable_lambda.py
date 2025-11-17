# python function to runnable comversion

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

def word_counter(text):
    return len(text.split())

runnable_word_counter=RunnableLambda(word_counter)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write joke on the topic {topic} in less than 50 words.",
    input_variables=["topic"]
)
parallel_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':runnable_word_counter
    }
)

chain=RunnableSequence(
    prompt,
    model,
    parser,
    parallel_chain,
)

result=chain.invoke({"topic":"space exploration"})
print(result)
chain.get_graph().print_ascii()