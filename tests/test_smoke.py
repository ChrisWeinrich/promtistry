"""Smoke tests for promtistry agents."""

import pytest

from promtistry.agents.builder import BuilderAgent
from promtistry.agents.judge import JudgeAgent


def test_builder_agent_smoke() -> None:
    """Test that BuilderAgent.run() can be called without error."""
    agent = BuilderAgent()
    result = agent.run()
    assert isinstance(result, str)


def test_judge_agent_smoke() -> None:
    """Test that JudgeAgent.run() can be called without error."""
    agent = JudgeAgent()
    result = agent.run()
    assert isinstance(result, str)
