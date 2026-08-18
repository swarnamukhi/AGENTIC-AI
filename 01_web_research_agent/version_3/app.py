from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langgraph.graph import StateGraph,START, END
import gradio as gr
import os


load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-120b",
             temperature=0)
search=TavilySearch(max_results=3)

@tool
def Calculator(a:int,b:int):
    """Add two numbers together."""
    result=a+b
    return result



model_with_tools=llm.bind_tools([search,Calculator])

class ResearchState(TypedDict):
    messages:Annotated[list,add_messages]

def AgentNode(State):
    response =model_with_tools.invoke(State["messages"])
    return {"messages": response}

# test_state = {
#     "messages": [HumanMessage(content="non sponcer jobs in uk ?")]
# }

# result = AgentNode(test_state)

#print(result)
tool_node = ToolNode([search,Calculator])

graph_builder = StateGraph(ResearchState)
graph_builder.add_node("agent", AgentNode)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "agent")

def should_continue(state):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"
    else:
        return "end"

graph_builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)

graph_builder.add_edge("tools", "agent")
graph = graph_builder.compile()
#graph.get_graph().print_ascii()


#user_input=input("enter user question")
def chatbot(user_input):
    result=graph.invoke({"messages":[HumanMessage(content=user_input)]})
    return result["messages"][-1].content

demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(
        label="Ask your Research Agent",
        placeholder="Ask a question..."
    ),
    outputs=gr.Textbox(
        label="Agent Response"
    ),
    title="Web Research Agent"
)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)

