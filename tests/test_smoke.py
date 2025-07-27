"""Smoke tests for promtistry agents."""

import pytest

from promtistry.agents.builder import BuilderAgent
from promtistry.agents.judge import JudgeAgent


def test_builder_agent_smoke() -> None:
    """Test that BuilderAgent.run() can be called without error."""
    agent = BuilderAgent()
    try:
        agent.run()
    except Exception as e:
        pytest.fail(f"BuilderAgent.run() raised an exception: {e}")


def test_judge_agent_smoke() -> None:
    """Test that JudgeAgent.run() can be called without error."""
    agent = JudgeAgent()
    try:
        agent.run()
    except Exception as e:
        pytest.fail(f"JudgeAgent.run() raised an exception: {e}")
