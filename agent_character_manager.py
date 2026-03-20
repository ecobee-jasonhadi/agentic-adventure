from strands import Agent, tool
from strands.models.gemini import GeminiModel
import os
from dotenv import load_dotenv
from strands_tools import file_write, file_read
from strands.multiagent.a2a import A2AServer

load_dotenv()

gemini = GeminiModel(
    client_args={"api_key": os.getenv("GEMINI_API_KEY")},
    model_id="gemini-2.5-flash",
)

DESCRIPTION = """
Specialized D&D character management agent that handles character creation, storage, and retrieval. 
Creates new characters with proper ability score generation (4d6 drop lowest), manages character data via character markdown files, 
and provides character lookup services. Maintains complete character profiles including stats, inventory, and progression data for D&D campaigns.
"""

SYSTEM_PROMPT = """
You are a D&D character management specialist. When creating characters, always roll ability scores using the traditional 
method: roll 4d6 and drop the lowest die for each of the six abilities (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma). 
Use the appropriate tools to create, find, or list characters as requested. Provide clear confirmations when characters are created and 
helpful summaries when characters are found. Keep responses focused and include relevant character details like class, race, and key stats."

Using file_read and file_write to retrieve and save characters in markdown files to the local filesystem.
"""


agent = Agent(
    model=gemini,
    tools=[file_read, file_write],
    description=DESCRIPTION,
    system_prompt=SYSTEM_PROMPT,
)

a2a_server = A2AServer(agent, host="0.0.0.0", port=8082)
a2a_server.serve()
