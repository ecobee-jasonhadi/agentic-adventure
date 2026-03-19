from strands import Agent
from strands.models.gemini import GeminiModel
import os
from dotenv import load_dotenv

load_dotenv()

gemini = GeminiModel(
    client_args={"api_key": os.getenv("GEMINI_API_KEY")},
    model_id="gemini-2.5-flash",
)

agent = Agent(model=gemini)

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
