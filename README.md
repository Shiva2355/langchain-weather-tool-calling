# 🌤️ LangChain Weather Tool Calling

A simple **LLM Tool Calling project** built with **LangChain + Google Gemini + OpenWeather API**.

The project demonstrates how an LLM can understand a user's request, decide when to use a tool, execute the tool, receive the result, and generate a final response.

## 🚀 How It Works

```text
User
  ↓
Gemini LLM
  ↓
Tool Call
  ↓
get_weather()
  ↓
OpenWeather API
  ↓
Tool Result
  ↓
Gemini LLM
  ↓
Final Answer
```

## 🛠️ Tech Stack

* Python
* LangChain
* Google Gemini
* OpenWeather API
* Requests
* python-dotenv

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd langchain-weather-tool-calling
```

Install dependencies:

```bash
pip install -U langchain langchain-google-genai python-dotenv requests
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Make sure `.env` is included in `.gitignore`:

```gitignore
.env
__pycache__/
venv/
```

Never commit API keys to GitHub.

## ▶️ Run the Project

```bash
python app.py
```

Example user query:

```text
What is the weather in Kakinada?
```

Example result:

```text
Location: Kākināda
Temperature: 31.31°C
Feels like: 37.81°C
Condition: light rain
Humidity: 68%
Wind speed: 5.4 m/s
```

## 🧠 Key Concepts Learned

### `@tool`

Converts a Python function into a LangChain tool.

```python
@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
```

### `bind_tools()`

Makes the tool available to the LLM.

```python
model_with_tools = model.bind_tools([get_weather])
```

### `invoke()`

Calls the model or executes a LangChain tool.

```python
response = model_with_tools.invoke(
    "What is the weather in Kakinada?"
)
```

### `ToolMessage`

Sends the tool execution result back to the LLM.

```python
tool_message = ToolMessage(
    content=tool_result,
    tool_call_id=tool_call["id"]
)
```

## 🔄 Tool Calling Flow

1. User asks a question.
2. Gemini receives the question.
3. Gemini decides whether a tool is required.
4. Gemini generates a tool call.
5. `get_weather()` executes.
6. OpenWeather API provides weather data.
7. The tool result is sent back to Gemini.
8. Gemini generates the final response.

## 📁 Project Structure

```text
langchain-weather-tool-calling/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

> `.env` should remain local and must not be committed to GitHub.

## 🎯 Purpose

This project was built to understand the fundamentals of **LLM Tool Calling**, including:

* Tool creation
* Tool schemas
* `bind_tools()`
* `tool_calls`
* Tool execution
* `ToolMessage`
* Multi-step LLM + Tool workflows

## 📚 Future Improvements

* Add more tools
* Add city geocoding
* Add database tools
* Add calculator tool
* Build a multi-tool AI agent
* Add a React frontend

## 👨‍💻 Author

Siva
