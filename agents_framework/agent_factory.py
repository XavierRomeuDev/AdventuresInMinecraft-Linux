from agent import Agent
from behaviors import ChatBehavior, InsultBehavior, TNTBehavior, MoveBehavior, BuildBehavior, DestroyBehavior

class AgentFactory:
    @staticmethod
    def create_agent(agent_type):
        if agent_type == "ChatBot":
            return Agent("ChatBot", ChatBehavior())
        elif agent_type == "InsultBot":
            return Agent("InsultBot", InsultBehavior())
        elif agent_type == "TNTBot":
            return Agent("TNTBot", TNTBehavior())
        elif agent_type == "MoverBot":
            return Agent("MoverBot", MoveBehavior())
        elif agent_type == "BuilderBot":
            return Agent("BuilderBot", BuildBehavior())
        elif agent_type == "DestroyerBot":
            return Agent("DestroyerBot", DestroyBehavior())
        else:
            raise ValueError(f"Agente desconocido: {agent_type}")
