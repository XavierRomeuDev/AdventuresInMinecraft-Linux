class Agent:
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior

    def perform_action(self, message=None):
        # El agente ejecuta su comportamiento, reaccionando al mensaje
        self.behavior.action(message)
