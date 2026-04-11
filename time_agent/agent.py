from datetime import datetime
from typing import Dict

from google.adk.agents.llm_agent import Agent
from google.adk.tools import FunctionTool


def get_current_time(city: str) -> Dict[str, str]:
    """
    Simple demo tool that returns the current time as a string.

    NOTE: This is a MOCK tool!
    It does NOT know real time zones for each city.
    It just returns your local time with the city name.
    """
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {
        "city": city,
        "time": current_time,
        "note": "Demo tool – using local system time, not real city timezone.",
    }

def simple_calculator(a: float, b: float, operation: str) -> Dict[str, str]:
    """
    A very simple calculator tool.
    Supported operations: add, sub, mul, div.
    """
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        if b == 0:
            return {"error": "Division by zero is not allowed."}
        result = a / b
    else:
        return {"error": "Unsupported operation. Use add, sub, mul, or div."}

    return {
        "a": str(a),
        "b": str(b),
        "operation": operation,
        "result": str(result),
    }

# Wrap our Python function as an ADK tool
time_tool = FunctionTool(get_current_time)
calc_tool = FunctionTool(simple_calculator)

# This is our root ADK agent
root_agent = Agent(
    model="gemini-2.5-flash",
    name="time_assistant",
    description="A friendly assistant that can chat and tell the time in a city using a tool.",
    instruction=(
        "You are a helpful assistant. "
        "When the user asks for the time in a city, call the get_current_time tool. "
	"When the user asks to do arithmetic with two numbers, call the simple_calculator tool. "
        "Otherwise, just answer normally."
    ),
    tools=[time_tool, calc_tool],
)
