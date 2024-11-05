import unittest
from unittest.mock import MagicMock
from agents_framework.agent import Agent
from agents_framework.agent_decorator import FireworkDecorator

class TestAgentDecorator(unittest.TestCase):
    def setUp(self):
        self.mock_agent = Agent("MockAgent", MagicMock())
        self.decorated_agent = FireworkDecorator(self.mock_agent)

    def test_perform_action_calls_decorated_action(self):
        self.mock_agent.perform_action = MagicMock()
        self.decorated_agent.perform_action("Test message")
        
        # Verificar que el decorador llama al método del agente original
        self.mock_agent.perform_action.assert_called_once_with("Test message")

    def test_firework_message(self):
        with unittest.mock.patch("mcpi.minecraft.Minecraft.postToChat") as mock_chat:
            self.decorated_agent.perform_action("Test message")
            mock_chat.assert_called_with("¡Lanzando fuegos artificiales!")
