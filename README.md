# Minimal DeepSeek Agent

A minimal AI Agent built from scratch using the DeepSeek API. 

## What it does
This project demonstrates the core **Tool Calling Loop** of an Agent, without relying on any heavy frameworks (like LangChain). 

The flow is:
1. The user asks a question.
2. The LLM decides to use a tool (e.g., an `add` function).
3. The Python code executes the function.
4. The result is fed back to the LLM to generate the final answer.

## Files
- `hello.py`: A basic test to verify API connectivity.
- `agent_tool.py`: The main script demonstrating the Agent tool-calling loop.

## How to run
1. Install dependencies: `pip install openai`
2. Set your API key as an environment variable: 
   `export DEEPSEEK_API_KEY="your_api_key_here"`
3. Run the script: `python agent_tool.py`
