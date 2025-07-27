"""Protocols for promtistry agents."""

from typing import Protocol

class Agent(Protocol):
    """Protocol for all promtistry agents."""

    def run(self) -> str:
        """Execute the agent's main logic.

        Returns:
            str: Result of the agent's execution.
        """
        ...
