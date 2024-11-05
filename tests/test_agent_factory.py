import unittest
from agents_framework.agent_factory import AgentFactory
from agents_framework.agent import Agent
from agents_framework.behaviors import ChatBehavior, InsultBehavior, TNTBehavior, MoveBehavior, BuildBehavior, DestroyBehavior

class TestAgentFactory(unittest.TestCase):
    def test_create_chatbot(self):
        agent = AgentFactory.create_agent("ChatBot")
        self.assertIsInstance(agent, Agent)
        self.assertIsInstance(agent.behavior, ChatBehavior)

    def test_create_insultbot(self):
        agent = AgentFactory.create_agent("InsultBot")
        self.assertIsInstance(agent, Agent)
        self.assertIsInstance(agent.behavior, InsultBehavior)

    def test_create_tntbot(self):
        agent = AgentFactory.create_agent("TNTBot")
        self.assertIsInstance(agent, Agent)
        self.assertIsInstance(agent.behavior, TNTBehavior)

    def test_invalid_agent_type(self):
        with self.assertRaises(ValueError):
            AgentFactory.create_agent("UnknownBot")
