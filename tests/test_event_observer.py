import unittest
from unittest.mock import MagicMock
from agents_framework.event_observer import EventObserver
from agents_framework.agent import Agent

class TestEventObserver(unittest.TestCase):
    def setUp(self):
        self.observer = EventObserver()
        self.mock_agent = Agent("MockAgent", MagicMock())

    def test_subscribe_agent(self):
        self.observer.subscribe(self.mock_agent)
        self.assertIn(self.mock_agent, self.observer._subscribers)

    def test_notify_agents(self):
        self.mock_agent.perform_action = MagicMock()
        self.observer.subscribe(self.mock_agent)
        self.observer.notify("Test message")
        
        # Verifica que el agente recibe la notificación
        self.mock_agent.perform_action.assert_called_once_with("Test message")
