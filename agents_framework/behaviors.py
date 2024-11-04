from abc import ABC, abstractmethod
import mcpi.minecraft as minecraft
import mcpi.block as block

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
        mc.postToChat(f"InsultBot dice: {message}, pero en realidad, ¡eres una tortuga!")

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
