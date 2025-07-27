from typing import Protocol, Any


class Agent(Protocol):
    """
    Protocol for all promtistry agents.
    """

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the agent's main logic.
        """
        ...
