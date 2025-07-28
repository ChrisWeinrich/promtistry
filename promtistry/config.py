"""Configuration module for the ChatBot."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Configuration data class for storing API settings."""

    api_key: str
    temperature: float
    model_name: str
    system_prompt: str | None


class ConfigService:
    """Service for managing configuration settings."""

    def __init__(self: "ConfigService") -> None:
        """Initialize ConfigService with environment variables."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            error_message = "OPENAI_API_KEY environment variable is not set"
            raise RuntimeError(error_message)
        temperature = float(os.getenv("CHATBOT_TEMPERATURE", "0.0"))
        model_name = os.getenv("CHATBOT_MODEL_NAME", "gpt-4.1")
        system_prompt = os.getenv("CHATBOT_SYSTEM_PROMPT") or None
        self.config = Config(
            api_key=api_key,
            temperature=temperature,
            model_name=model_name,
            system_prompt=system_prompt,
        )

    def get_config(self: "ConfigService") -> Config:
        """Retrieve the current configuration."""
        return self.config


config_service = ConfigService()
