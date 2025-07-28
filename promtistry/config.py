"""Configuration module for the ChatBot."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Configuration data class for storing API settings."""

    api_key: str
    builder_temperature: float
    builder_model_name: str
    builder_system_prompt: str | None
    judge_temperature: float
    judge_model_name: str
    judge_system_prompt: str | None
    judge_score_threshold: float


class ConfigService:
    """Service for managing configuration settings."""

    def __init__(self: "ConfigService") -> None:
        """Initialize ConfigService with environment variables."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            error_message = "OPENAI_API_KEY environment variable is not set"
            raise RuntimeError(error_message)

        # Builder settings
        builder_temperature = float(os.getenv("BUILDER_TEMPERATURE", "0.0"))
        builder_model_name = os.getenv("BUILDER_MODEL_NAME", "gpt-4.1")
        builder_system_prompt = os.getenv("BUILDER_SYSTEM_PROMPT") or None

        # Judge settings
        judge_temperature = float(os.getenv("JUDGE_TEMPERATURE", "0.0"))
        judge_model_name = os.getenv("JUDGE_MODEL_NAME", "gpt-4.1")
        judge_system_prompt = os.getenv("JUDGE_SYSTEM_PROMPT") or None
        judge_score_threshold = float(os.getenv("JUDGE_SCORE_THRESHOLD", "4.0"))

        self.config = Config(
            api_key=api_key,
            builder_temperature=builder_temperature,
            builder_model_name=builder_model_name,
            builder_system_prompt=builder_system_prompt,
            judge_temperature=judge_temperature,
            judge_model_name=judge_model_name,
            judge_system_prompt=judge_system_prompt,
            judge_score_threshold=judge_score_threshold,
        )

    def get_config(self: "ConfigService") -> Config:
        """Retrieve the current configuration."""
        return self.config


config_service = ConfigService()
