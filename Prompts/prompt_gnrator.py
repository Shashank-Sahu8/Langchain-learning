from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template="""Write a {paper_type} on the topic of {topic} with a length of {length} words.""",
    input_variables=["paper_type", "topic", "length"]
)

template.save("template.json")