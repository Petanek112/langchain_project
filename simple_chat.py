from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

# Load .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Please set OPENAI_API_KEY in your .env file!")

model = init_chat_model(
    model="chatgpt-4",
    model_provider="openai",
    api_key=api_key,
    temperature=0.7,
)

response = model.invoke("Hello, how are you?")
print(response.content)