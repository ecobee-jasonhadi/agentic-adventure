from strands import Agent, tool
from strands.models.gemini import GeminiModel
import os
from dotenv import load_dotenv
import random
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamable_http_client

load_dotenv()

gemini = GeminiModel(
    client_args={"api_key": os.getenv("GEMINI_API_KEY")},
    model_id="gemini-2.5-flash",
)

dice_mcp = MCPClient(lambda: streamable_http_client("http://0.0.0.0:8081/mcp"))

agent = Agent(model=gemini, tools=[dice_mcp])

print("Agentic Adventure - Type 'quit' to exit")
while True:
    try:
        user_input = input("\n> ")
    except (EOFError, KeyboardInterrupt):
        print("\nFarewell, adventurer!")
        break
    if user_input.strip().lower() in ("quit", "exit"):
        print("Farewell, adventurer!")
        break
    if not user_input.strip():
        continue
    agent(user_input)
