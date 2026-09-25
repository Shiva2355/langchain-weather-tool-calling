from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import json
import requests
from langchain.tools import tool
from langchain.messages import ToolMessage
import pprint
load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
##create the model
model=init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    api_key=GEMINI_API_KEY
)

api_key=os.getenv("api_key")
#function with tool creation given description also
@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    url=f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    response=requests.get(url)
    data=response.json()

    city = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    return (
        f"Location: {city}\n"
        f"Temperature: {temperature}°C\n"
        f"Feels like: {feels_like}°C\n"
        f"Condition: {weather}\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind_speed} m/s"
    )


from langchain_core.messages import HumanMessage, ToolMessage

model_with_tools = model.bind_tools([get_weather])

# User message
user_message = HumanMessage(
    content="What is the weather in Peddapuram?"
)

# LLM call #1
response = model_with_tools.invoke([
    user_message
])

print("TOOL CALL:")
print(response.tool_calls)

# Execute tool
tool_call = response.tool_calls[0]

tool_result = get_weather.invoke(
    tool_call["args"]
)

print("\nTOOL RESULT:")
print(tool_result)

# Tool result
tool_message = ToolMessage(
    content=tool_result,
    tool_call_id=tool_call["id"]
)

# LLM call #2
final_response = model_with_tools.invoke([
    user_message,
    response,
    tool_message
])

print("\nFINAL ANSWER:")
print(final_response.content)