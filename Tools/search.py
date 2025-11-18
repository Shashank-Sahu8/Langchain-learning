from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

result = search_tool.invoke("Who is Shashank Sahu?")

print(result)