from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages=[
    SystemMessage(content="You are a doctor and you help providing medical advice.Remember you dont reply to any other queries say not able to help."),
    HumanMessage(content="What should I do I am suffering from fungal infection?")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)