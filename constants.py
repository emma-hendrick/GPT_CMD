# OS allows us to retrieve our environment variables
import os

# All the program constants
class CONST:
    GPT_KEY = os.environ["GPT_KEY"]
    GPT_URL = "https://api.openai.com/v1/chat/completions"
    GPT_MODEL = "gpt-3.5-turbo"
    GPT_TEMPERATURE = 0.7
