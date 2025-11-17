from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="Generate a simple story about {topic} with a length of {length} words.",
    input_variables=["topic", "length"]
)

prompt2=PromptTemplate(
    template="Generate the 5 questions and answers for a quiz on the topic of {topic}.",
    input_variables=["topic"]
)

prompt3=PromptTemplate(
    template="Merge the story and the quiz into a single document.{story}and {quiz}",
    input_variables=["story", "quiz"]
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        "story": prompt1 | model | parser,
        "quiz": prompt2 | model | parser
    }
)

merged_chain= parallel_chain | prompt3 | model | parser

result= merged_chain.invoke({
    "topic":"Space Exploration",    
    "length":300
})

print(result)

merged_chain.get_graph().print_ascii()