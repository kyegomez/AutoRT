import os
from swarms import Gemini, GPT4VisionAPI, OpenAIChat
from autort.prompts import VISUALIZE_OBJECT_PROMPT, GENERATE_TASKS_PROMPT
from dotenv import load_dotenv

load_dotenv()

max_tokens = 1000
gemini = Gemini(gemini_api_key=os.getenv("GEMINI_API_KEY"))
gpt4v = GPT4VisionAPI(
    system_prompt=VISUALIZE_OBJECT_PROMPT,
    openai_api_key=os.getenv("OPENAI_API_KEY"), 
    max_tokens=max_tokens
)
openaichat = OpenAIChat(
    openai_api_key=os.getenv("OPENAI_API_KEY"), 
    max_tokens=max_tokens
)




