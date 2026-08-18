import os
from dotenv import load_dotenv

load_dotenv()

print("groq key loaded",bool(os.getenv("GROQ_API_KEY")))
print("Travily key loaded",bool(os.getenv("TAVILY_API_KEY")))