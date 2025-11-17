from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro")

result=model.invoke("Who is Shashank Sahu a software engineer and a popular student?")

print(result.content)

