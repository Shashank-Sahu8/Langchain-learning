from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableBranch, RunnableSequence,  RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="write a detailed report on the topic {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="summarize the following report in less than 50 words: {report}",
    input_variables=["report"]
)

report_genration_chain=RunnableSequence(
    prompt1,
    model,
    parser
)

# alternate of above command is presented below:
# report_genration_chain=prompt1|model|parser

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain=RunnableSequence(report_genration_chain,branch_chain)

result=chain.invoke({"topic":"Poverty level in India"})