"""ChatBot agent using LangChain and OpenAI."""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI


class ChatAgent:
    """ChatBot agent using LangChain and OpenAI."""

    def __init__(self: "ChatAgent", api_key: str) -> None:
        """Initialize ChatAgent with LLM and memory."""
        self.llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)

    def run(self: "ChatAgent", message: str) -> str:
        """Send user message to the conversation chain and return the response."""
        response = self.chain.predict(input=message)
        return str(response)
