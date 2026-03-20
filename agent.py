from strands import Agent
from strands.models.gemini import GeminiModel

model = GeminiModel(
    client_args={"api_key": ""},
    model_id="gemini-2.5-flash",
)

agent = Agent(model=model)

agent("Hello from Toronto! How are you?")
