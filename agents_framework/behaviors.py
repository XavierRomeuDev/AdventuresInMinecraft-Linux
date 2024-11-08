from abc import ABC, abstractmethod
import mcpi.minecraft as minecraft
import mcpi.block as block
from functools import reduce
import time
import inspect

# Conexión a Minecraft
mc = minecraft.Minecraft.create()

# Clase abstracta para definir el comportamiento (Strategy)
class Behavior(ABC):
    @abstractmethod
    def action(self, message=None):
        pass

# Comportamiento de un agente que envía mensajes al chat
class ChatBehavior(Behavior):
    def action(self, message=None):
        mc.postToChat(f"ChatBot ha recibido: {message}")

# Comportamiento de un agente que insulta en el chat
class InsultBehavior(Behavior):
    def action(self, message=None):
        mc.postToChat(f"InsultBot dice: {message}, bien, pero en realidad, ¡eres un mal programador!")

# Comportamiento de un agente que coloca TNT y la activa
class TNTBehavior(Behavior):
    def action(self, message=None):
        try:
            # Posición fija del jugador (ejemplo: coordenadas X=10, Y=5, Z=10)
            pos_x = 10
            pos_y = 5
            pos_z = 10

            # Colocar TNT en una posición fija
            mc.setBlock(pos_x + 1, pos_y, pos_z, block.TNT.id)

            # Enviar un mensaje al chat
            mc.postToChat(f"TNTBot ha recibido: {message}")
        except Exception as e:
            mc.postToChat(f"Error al colocar TNT: {str(e)}")
            print(f"Error: {e}")

# Comportamiento de movimiento
class MoveBehavior(Behavior):
    def action(self, message=None):
        # Movimiento simple: mover hacia adelante en el eje X
        pos_x = 10
        pos_y = 5
        pos_z = 10
        new_pos = pos_x + 1, pos_y, pos_z
        # hauriem de tenir un usuari actiu dins el servidor per poder accedir a la seva posició
        # mc.player.setTilePos(*new_pos)
        mc.postToChat(f"MoveBehavior: Agente movido a la posición {new_pos}")

# Comportamiento de construcción
class BuildBehavior(Behavior):
    def action(self, message=None):
        # Construir una torre de bloques de piedra
        pos_x = 10
        pos_y = 5
        pos_z = 10
        for y in range(pos_y, pos_y + 5):
            mc.setBlock(pos_x + 2, y, pos_z, block.STONE.id)
        mc.postToChat("BuildBehavior: Torre de piedra construida.")

# Comportamiento de destrucción
class DestroyBehavior(Behavior):
    def action(self, message=None):
        # Destruir un bloque específico
        pos_x = 10
        pos_y = 5
        pos_z = 10       
        mc.setBlock(pos_x - 2, pos_y, pos_z, block.AIR.id)
        mc.postToChat("DestroyBehavior: Bloque destruido.")


#Comportament per demostrar l'ús de la programació funcional
class FunctionalBehavior(Behavior):
    def __init__(self, actions):
        self.actions = actions

    def action(self, message=None):
        pos = (10, 5, 10)
        mc.postToChat(f"FunctionalAgent comienza en la posición {pos}")

        # Filtrar acciones que cambiarían la posición
        filtered_actions = filter(lambda action: action(pos) != pos, self.actions)

        # Aplicar las acciones filtradas secuencialmente con reduce
        final_pos = reduce(lambda acc, action: action(acc), filtered_actions, pos)

        mc.postToChat(f"FunctionalAgent ha terminado en la posición {final_pos}")
        time.sleep(1)  # Pausa corta para reducir conflictos de concurrencia

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

# Funciones de acción para el agente funcional
def move_forward(pos):
    # Solo mover si x es par
    if pos[0] % 2 == 0:
        new_pos = (pos[0] + 1, pos[1], pos[2])
        mc.postToChat(f"FunctionalAgent se mueve a {new_pos}")
        return new_pos
    return pos  # Sin cambio si no se cumple la condición

def build_block(pos):
    # Solo construir si y es menor que 10
    if pos[1] < 10:
        new_pos = (pos[0], pos[1] + 1, pos[2])
        mc.postToChat(f"FunctionalAgent construye en {new_pos}")
        return new_pos
    return pos  # Sin cambio si no se cumple la condición

def destroy_block(pos):
    # Solo destruir si z es múltiplo de 5
    if pos[2] % 5 == 0:
        new_pos = (pos[0], pos[1] - 1, pos[2])
        mc.postToChat(f"FunctionalAgent destruye en {new_pos}")
        return new_pos
    return pos  # Sin cambio si no se cumple la condición
