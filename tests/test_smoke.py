from promtistry.agents.builder import BuilderAgent
from promtistry.agents.judge import JudgeAgent


def test_builder_agent_smoke():
    agent = BuilderAgent()
    # Just check that run() can be called without error
    try:
        agent.run()
    except Exception as e:
        assert False, f"BuilderAgent.run() raised an exception: {e}"


def test_judge_agent_smoke():
    agent = JudgeAgent()
    # Just check that run() can be called without error
    try:
        agent.run()
    except Exception as e:
        assert False, f"JudgeAgent.run() raised an exception: {e}"
