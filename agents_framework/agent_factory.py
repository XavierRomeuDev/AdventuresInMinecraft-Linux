from agent import Agent
from behaviors import ChatBehavior, FunctionalBehavior, ReflectiveBehavior, InsultBehavior, TNTBehavior, MoveBehavior, BuildBehavior, DestroyBehavior, move_forward, build_block, destroy_block

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
        elif agent_type == "FunctionalAgent":
            actions = [move_forward, build_block, destroy_block]
            return Agent("FunctionalAgent", FunctionalBehavior(actions))
        elif agent_type == "ReflectiveAgent":
            agent = Agent("ReflectiveAgent", ReflectiveBehavior(agent=None))
            agent.behavior.agent = agent  # Asigna el agente a su comportamiento reflexivo
            return agent
        else:
            raise ValueError(f"Agente desconocido: {agent_type}")
