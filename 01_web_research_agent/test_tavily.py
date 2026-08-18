import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
load_dotenv()

search =TavilySearch(max_results=3)

response =search.invoke("latest developemtment in AI agents")

print(response)
