from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

print(multiply.invoke({"a": 6, "b": 7}))

model_with_tools=model.bind_tools([multiply])

