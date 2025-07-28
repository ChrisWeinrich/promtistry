"""LangGraph flow for chat interactions."""

from langgraph.graph import END, StateGraph

from promtistry.agents.chat_agent import ChatAgent
from promtistry.config import config_service
from promtistry.flow.state import ChatState

config = config_service.get_config()

agent = ChatAgent(
    api_key=config.api_key,
    temperature=config.temperature,
    model_name=config.model_name,
    system_prompt=config.system_prompt,
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
