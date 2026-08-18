import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-120b",
             temperature=0)

search=TavilySearch(max_results=3)
def main():
        user_question=input("enter the research question")
        search_results=search.invoke(user_question)

        prompt=f""" you are research analyst

        research question:{user_question}
        here are the web research result:{search_results}

        using the web search result create a clear answer to the user quesion
        include:
        1.summer
        2.key finding
        3.sources mentioned in the search results


        do not invent information that is not supported by the web results


        """

        print("Generating research report\n")
        response =llm.invoke(prompt)
        print("=" * 60)
        print("RESEARCH REPORT")
        print("=" * 60)

        print(response.content)
if __name__=="__main__":
        main()    


