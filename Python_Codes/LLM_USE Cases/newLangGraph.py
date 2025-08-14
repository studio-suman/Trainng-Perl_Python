from typing import Annotated

from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    base_url='AZURE_OPENAI_ENDPOINT',
    api_key= ['AZURE_OPENAI_API_KEY'], # type: ignore
    model= 'AZURE_OPENAI_DEPLOYMENT_NAME',
)

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def node4(state):
    pass

graph_builder.add_node("node_4", node4)  # Add node for node4
# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)  # Add node for chatbot


graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")


graph = graph_builder.compile()

graph_builder.add_edge("start", "node_4")
graph_builder.add_edge("node_4", "chatbot")