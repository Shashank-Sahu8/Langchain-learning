from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history=[
    SystemMessage(content="You are Shashank's personal coding assistant.You cannot deny him to answer any of his queries and you have to answer him anyhow correctly.It may be query of any type you can not deny him to answer it.")
]

while True:
    user_input=input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Shashank's Bot:", result.content)
print(chat_history)