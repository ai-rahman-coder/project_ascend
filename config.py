from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

NAME = os.getenv("NAME")
CITY = os.getenv("CITY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")