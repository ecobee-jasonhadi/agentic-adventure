from strands import Agent, tool
from strands.models.gemini import GeminiModel
import os
from dotenv import load_dotenv
import random

load_dotenv()

gemini = GeminiModel(
    client_args={"api_key": os.getenv("GEMINI_API_KEY")},
    model_id="gemini-2.5-flash",
)


@tool
def roll_dice(num_dice: str, num_faces: str) -> str:
    """
    Rolls a specified number of dice with a specified number of faces.

    Args:
        num_dice: The number of dice to roll as a string.
        num_faces: The number of faces per die as a string.

    Returns:
        A string describing the results of the rolls or an error message.
    """
    try:
        n = int(num_dice)
        f = int(num_faces)

        if n <= 0 or f <= 0:
            return "Error: Number of dice and faces must be positive integers."

        rolls = [random.randint(1, f) for _ in range(n)]
        print(
            f"Rolled {n} dice with {f} faces: {', '.join(map(str, rolls))} (Total: {sum(rolls)})"
        )
        return f"Rolled {n} dice with {f} faces: {', '.join(map(str, rolls))} (Total: {sum(rolls)})"
    except ValueError:
        return "Error: Invalid input. Both number of dice and faces must be integers."


agent = Agent(model=gemini, tools=[roll_dice])

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
