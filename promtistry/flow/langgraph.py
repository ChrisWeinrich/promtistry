"""LangGraph flow for chat interactions."""

import os

from langgraph.graph import END, StateGraph

from promtistry.agents.chat_agent import ChatAgent
from promtistry.flow.state import ChatState

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    error_message = "OPENAI_API_KEY environment variable is not set"
    raise RuntimeError(error_message)

agent = ChatAgent(
    api_key=api_key,
    temperature=0.7,
    model_name="gpt-4o-mini",
)


def bot_node(state: ChatState) -> ChatState:
    """Take `user_msg`, call the LLM, and return `bot_msg`.

    If the user types "exit", set a farewell message,
    but do NOT call the LLM anymore.
    """
    if not state.user_msg:  # empty input = do nothing
        return state

    if state.user_msg.strip().lower() == "exit":
        # We send a farewell message …
        return state.update(bot_msg="See you soon! 👋")

    answer: str = agent.run(state.user_msg)
    return state.update(bot_msg=answer)


# ----- Graph ----------------------------------------------------------------
graph = StateGraph(state_schema=ChatState)
graph.add_node("bot", bot_node)
graph.set_entry_point("bot")


# After one bot invocation, terminate the graph
graph.add_edge("bot", END)

runner = graph.compile()
__all__ = ["runner"]
