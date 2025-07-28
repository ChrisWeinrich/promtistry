"""LangGraph flow for chat interactions."""

import logging

from langgraph.graph import StateGraph

from promtistry.agents.chat_agent import ChatAgent
from promtistry.config import config_service
from promtistry.flow.state import ChatState

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

config = config_service.get_config()

# Two agents: Prompt-Builder and Judge
builder_agent = ChatAgent(
    api_key=config.api_key,
    temperature=config.builder_temperature,
    model_name=config.builder_model_name,
    system_prompt=config.builder_system_prompt,
)
judge_agent = ChatAgent(
    api_key=config.api_key,
    temperature=config.judge_temperature,
    model_name=config.judge_model_name,
    system_prompt=config.judge_system_prompt,
)


def bot_node(state: ChatState) -> ChatState:
    """Take `user_msg`, call the LLM, and return `bot_msg`.

    If the user types "exit", set a farewell message,
    but do NOT call the LLM anymore.
    """
    logger.debug("Entering bot_node with state: %s", state)
    if not state.user_msg:  # empty input = do nothing
        return state

    if state.user_msg.strip().lower() == "exit":
        # We send a farewell message …
        return state.update(bot_msg="See you soon! 👋")

    logger.debug("bot_node calling builder_agent with user_msg: %s", state.user_msg)
    answer: str = builder_agent.run(state.user_msg)
    logger.debug("bot_node received answer: %s", answer)
    return state.update(bot_msg=answer)


def judge_node(state: ChatState) -> ChatState:
    """Take `bot_msg`, call the Judge LLM, and return `judge_msg`."""
    logger.debug("Entering judge_node with state: %s", state)
    if not state.bot_msg:
        return state
    logger.debug("judge_node calling judge_agent with bot_msg: %s", state.bot_msg)
    instruction = f"Please evaluate the following prompt:\n{state.bot_msg}"
    evaluation: str = judge_agent.run(instruction)
    logger.debug("judge_node received evaluation: %s", evaluation)
    return state.update(judge_msg=evaluation)


# ----- Graph ----------------------------------------------------------------
graph = StateGraph(state_schema=ChatState)
graph.add_node("bot", bot_node)
graph.set_entry_point("bot")

# (Judge is invoked separately via UI; no automatic judge step in the flow)

runner = graph.compile()
__all__ = ["runner"]
