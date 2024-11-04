class EventObserver:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, agent):
        """Suscribir un agente a los eventos."""
        self._subscribers.append(agent)

    def notify(self, message):
        """Notificar a todos los agentes sobre un evento."""
        for agent in self._subscribers:
            agent.perform_action(message)
