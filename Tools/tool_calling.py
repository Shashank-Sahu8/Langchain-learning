from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

# print(multiply.invoke({"a": 6, "b": 7}))

model_with_tools=model.bind_tools([multiply])

query=HumanMessage(content="multiply 6 and 7")

messages=[query]

result=model_with_tools.invoke(messages)

messages.append(result)

# print(messages)

tool_result=multiply.invoke(result.tool_calls[0])

messages.append(tool_result)
# print(messages)
# print(multiply_result)
ans=model_with_tools.invoke(messages)
print(ans)