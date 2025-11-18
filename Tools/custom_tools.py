from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field
# #create fuction
# def multiply(a,b) -> int:
#     """Multiplies two numbers."""
#     return a * b

# #type hunting
# def multiply(a:int,b:int) -> int:
#     """Multiplies two numbers."""
#     return a * b

# #add decorators


# using tool decorator

@tool
def multiply(a:int,b:int) -> int:
    """Multiplies two numbers."""
    return a * b

# result=multiply.invoke({"a":6,"b":7})
# print(result)

# print(multiply.description)
# print(multiply.name)


# using structured tool and pydantic model strict inforcement

class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")
    
def multiply(a:int,b:int) -> int:
    """Multiplies two numbers."""
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiplies two numbers.",
    input_schema=MultiplyInput
)

# result=multiply_tool.invoke({"a":6,"b":7})
# print(result)


#using base tool class

class MultiplyTool(BaseTool):
    name:str = "multiply"
    description:str = "Multiplies two numbers."

    class MultiplyInput(BaseModel):
        a: int = Field(..., description="The first number to multiply")
        b: int = Field(..., description="The second number to multiply")

    def _run(self, a: int, b: int) -> int:
        """Multiplies two numbers."""
        return a * b

    

multiply_tool_base = MultiplyTool()

result=multiply_tool_base.invoke({"a":6,"b":7})
print(result)