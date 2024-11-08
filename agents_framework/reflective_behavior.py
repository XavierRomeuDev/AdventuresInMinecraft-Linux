import inspect

class ReflectiveBehavior(Behavior):
    def __init__(self, agent):
        self.agent = agent

    def action(self, message=None):
        mc.postToChat("ReflectiveAgent ha recibido un mensaje de inspección.")
        
        # Inspeccionar atributos y métodos del agente
        attributes = dir(self.agent)
        mc.postToChat(f"Atributos del agente: {attributes}")
        
        # Ejecutar un método dinámicamente, si el mensaje coincide con el nombre de un método
        if hasattr(self.agent, message) and callable(getattr(self.agent, message)):
            method = getattr(self.agent, message)
            mc.postToChat(f"Ejecutando método {message} dinámicamente.")
            method()
        
        # Modificar un atributo dinámicamente
        if hasattr(self.agent, "name"):
            setattr(self.agent, "name", "ReflectiveAgentModificado")
            mc.postToChat(f"El nombre del agente ha sido modificado a: {self.agent.name}")
