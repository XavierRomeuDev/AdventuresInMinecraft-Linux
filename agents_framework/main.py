from agent_factory import AgentFactory
from event_observer import EventObserver
from agent_decorator import FireworkDecorator


# Crear el observador de eventos
event_observer = EventObserver()

# Crear agentes usando la fábrica y suscribirlos al observador
chat_bot = AgentFactory.create_agent("ChatBot")
insult_bot = AgentFactory.create_agent("InsultBot")
tnt_bot = AgentFactory.create_agent("TNTBot")
mover_bot = AgentFactory.create_agent("MoverBot")
builder_bot = AgentFactory.create_agent("BuilderBot")
destroyer_bot = AgentFactory.create_agent("DestroyerBot")
functional_agent = AgentFactory.create_agent("FunctionalAgent")
reflective_agent = AgentFactory.create_agent("ReflectiveAgent")


# Añadirle la habilidad extra de lanzar fuegos artificiales
firework_chat_bot = FireworkDecorator(chat_bot)

event_observer.subscribe(chat_bot)
event_observer.subscribe(insult_bot)
event_observer.subscribe(tnt_bot)
event_observer.subscribe(firework_chat_bot)
event_observer.subscribe(mover_bot)
event_observer.subscribe(builder_bot)
event_observer.subscribe(destroyer_bot)
event_observer.subscribe(functional_agent)
event_observer.subscribe(reflective_agent)

message_agent_map = {
    "Hola": [chat_bot],
    "¿Cómo estás?": [insult_bot],
    "Explota esto": [tnt_bot],
    "Construye una torre": [builder_bot],
    "Lanzar fuegos artificiales": [chat_bot, firework_chat_bot],
    "Ejecutar acciones funcionales": [functional_agent]
}

# Método para notificar a agentes específicos en el EventObserver
def notify_specific_agents(message):
    agents = message_agent_map.get(message, [])
    for agent in agents:
        agent.perform_action(message)

simulated_messages = ["Hola", "¿Cómo estás?", "Explota esto", "Construye una torre", "Lanzar fuegos artificiales", "Ejecutar acciones funcionales"]

for message in simulated_messages:
    print(f"Recibiendo mensaje: {message}")
    notify_specific_agents(message)  # Notificar solo a agentes específicos

event_observer.notify("action")  # Este mensaje simula la llamada a su propio método "action"

# Bucle infinito para mantener la conexión abierta y procesar mensajes
import time
while True:
        time.sleep(10)  # Espera antes del próximo mensaje
