from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage,HumanMessage

load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile",
             temperature=0)
search=TavilySearch(max_results=3)

model_with_tools=llm.bind_tools([search])

def main():
    user_question=input("enter the research question that you wanted to search ")
    groq_response=model_with_tools.invoke(user_question)
    #print(response)
    tool_call = groq_response.tool_calls[0]
    #print(tool_call["name"])
    #print(tool_call["args"])

    tavily_response=search.invoke(tool_call['args'])
    #print(tavily_response)
    tool_message= ToolMessage(content=str(tavily_response),
                              tool_call_id=tool_call['id'])
    message=[HumanMessage(content=user_question),groq_response,tool_message,HumanMessage(content="""
    Using the web search result, create a clear answer.

    Include:
    1. Summary
    2. Key findings
    3. Sources mentioned in the search results

    Do not invent information that is not supported by the web results.
    """)]
    final_response=model_with_tools.invoke(message)
    print(final_response.content)
    #print(tool_message)
if __name__=='__main__':
    main()
