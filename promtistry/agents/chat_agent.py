"""ChatBot agent using LangChain and OpenAI."""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI


class ChatAgent:
    """ChatBot agent using LangChain and OpenAI."""

    def __init__(
        self: "ChatAgent",
        api_key: str,
        temperature: float = 0.0,
        model_name: str = "gpt-4.1",
        system_prompt: str | None = None,
    ) -> None:
        """Initialize ChatAgent with LLM, memory, and system prompt."""
        self.llm = ChatOpenAI(
            temperature=temperature,
            openai_api_key=api_key,
            model_name=model_name,
        )
        self.memory = ConversationBufferMemory(return_messages=True)
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)
        self.system_prompt = system_prompt

    def run(self: "ChatAgent", message: str) -> str:
        """Send user message to the conversation chain and return the response."""
        if self.system_prompt and not self.memory.buffer:
            # inject system prompt as the first message
            self.chain.predict(input=self.system_prompt)
        return str(self.chain.predict(input=message))
