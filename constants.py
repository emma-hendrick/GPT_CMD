# OS allows us to retrieve our environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load variables from .env
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# All the program constants
class CONST:
    GPT_KEY = os.environ["GPT_KEY"]
    GPT_URL = "https://api.openai.com/v1/chat/completions"
    GPT_MODEL = "gpt-3.5-turbo"
    GPT_TEMPERATURE = 0.7
