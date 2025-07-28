"""State management for chat flow."""

from dataclasses import dataclass, replace


@dataclass(frozen=True, slots=True)
class ChatState:
    """Minimal, immutable state for the bot flow."""

    user_msg: str = ""
    bot_msg: str = ""

    def update(self: "ChatState", **changes: str) -> "ChatState":
        """Update the chat state with new values."""
        return replace(self, **changes)
