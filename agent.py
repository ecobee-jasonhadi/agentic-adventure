from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import current_time, file_write, python_repl

model = GeminiModel(
    client_args={"api_key": ""},
    model_id="gemini-2.5-flash",
)

agent = Agent(model=model, tools=[current_time, file_write, python_repl])

agent(
    "Write a python file that calculates 5 iterations of the fibbonaci sequence and save it to a local file. Execute the python file."
)
