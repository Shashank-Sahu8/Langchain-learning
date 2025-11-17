from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("Who is Shashank Sahu?")

print(result)


# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# result = llm.invoke("Who is Shashank Sahu?")

# print(result.content)
