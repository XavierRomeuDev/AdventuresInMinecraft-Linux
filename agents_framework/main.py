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

# Añadirle la habilidad extra de lanzar fuegos artificiales
firework_chat_bot = FireworkDecorator(chat_bot)

event_observer.subscribe(chat_bot)
event_observer.subscribe(insult_bot)
event_observer.subscribe(tnt_bot)
event_observer.subscribe(firework_chat_bot)
event_observer.subscribe(mover_bot)
event_observer.subscribe(builder_bot)
event_observer.subscribe(destroyer_bot)

# Simulación de mensajes del chat (en el futuro, esto vendría del chat de Minecraft)
simulated_messages = ["Hola", "¿Cómo estás?", "Explota esto", "Construye una torre", "¿Quién creó Minecraft?"]

for message in simulated_messages:
        print(f"Recibiendo mensaje: {message}")
        event_observer.notify(message)  # Notificar a los agentes sobre el mensaje

# Bucle infinito para mantener la conexión abierta y procesar mensajes
import time
while True:
        time.sleep(10)  # Espera antes del próximo mensaje
