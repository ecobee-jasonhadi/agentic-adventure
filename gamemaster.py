from strands import Agent, tool
from strands.models.gemini import GeminiModel
import os
from dotenv import load_dotenv
import random
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamable_http_client
from strands_tools.a2a_client import A2AClientToolProvider

load_dotenv()

gemini = GeminiModel(
    client_args={"api_key": os.getenv("GEMINI_API_KEY")},
    model_id="gemini-3.1-flash-lite-preview",
    params={"temperature": "0.5"},
)

dice_mcp = MCPClient(lambda: streamable_http_client("http://0.0.0.0:8081/mcp"))

a2a_provider = A2AClientToolProvider(
    known_agent_urls=[
        "http://0.0.0.0:8082",
        "http://0.0.0.0:8083",
    ]
)

SYSTEM_PROMPT = """You are a D&D Game Master orchestrator with access to specialized agents and tools.

Available agents:
- Character Agent (http://0.0.0.0:8082) - For character creation and management
- Rules Agent (http://0.0.0.0:8083) - For rule referencing and validating game mechanics

To communicate with agents:
1. Use a2a_list_discovered_agents to see available agents
2. Use a2a_send_message with the agent's URL to send questions
3. Use roll_dice for dice rolling

Available D&D dice types:
- d4 (4-sided die) - Used for damage rolls of small weapons like daggers
- d6 (6-sided die) - Used for damage rolls of weapons like shortswords, spell damage
- d8 (8-sided die) - Used for damage rolls of weapons like longswords, rapiers
- d10 (10-sided die) - Used for damage rolls of heavy weapons, percentile rolls
- d12 (12-sided die) - Used for damage rolls of great weapons like greataxes
- d20 (20-sided die) - Used for ability checks, attack rolls, saving throws
- d100 (percentile die) - Used for random tables, wild magic surges

IMPORTANT: Always use the exact URLs shown by a2a_list_discovered_agents. Never invent or guess URLs.

Be creative, engaging, and use your available tools to enhance the D&D experience.
You must roll dice when asked to provide the results to the user or to other agents.
Always consult the rules agent when executing mechanics or dice rolls in the game.

"""


agent = Agent(
    model=gemini, tools=[dice_mcp] + a2a_provider.tools, system_prompt=SYSTEM_PROMPT
)

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
