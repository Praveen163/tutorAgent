
from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel
import os
load_dotenv()
google_api_key = "AIzaSyBMDSTsqb2mKJ57jk5PcDY4Wk1vYN6uZ8s"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=gemini_client)