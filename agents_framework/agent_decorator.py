from agent import Agent
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

# Clase base para los decoradores
class AgentDecorator(Agent):
    def __init__(self, agent):
        self._agent = agent

    def perform_action(self, message=None):
        # Llamamos a la acción del agente original
        self._agent.perform_action(message)

# Decorador que añade la habilidad de lanzar fuegos artificiales
class FireworkDecorator(AgentDecorator):
    def perform_action(self, message=None):
        # Ejecuta la acción del agente original
        super().perform_action(message)
        # Añadimos la funcionalidad extra: lanzar fuegos artificiales
        mc.postToChat("¡Lanzando fuegos artificiales!")
        # Aquí podrías añadir la lógica para mostrar los fuegos artificiales
