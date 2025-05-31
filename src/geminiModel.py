from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
load_dotenv()
google_api_key = os.getenv("OPENAI_API_KEY") #Google GEMINI API Key
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)
