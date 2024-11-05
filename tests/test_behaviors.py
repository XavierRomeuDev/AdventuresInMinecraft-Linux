import unittest
from unittest.mock import patch
from agents_framework.behaviors import ChatBehavior, InsultBehavior, TNTBehavior, MoveBehavior, BuildBehavior, DestroyBehavior

class TestBehaviors(unittest.TestCase):
    @patch("mcpi.minecraft.Minecraft.postToChat")
    def test_chat_behavior(self, mock_chat):
        behavior = ChatBehavior()
        behavior.action("Hello")
        mock_chat.assert_called_with("ChatBot ha recibido: Hello")

    @patch("mcpi.minecraft.Minecraft.postToChat")
    def test_insult_behavior(self, mock_chat):
        behavior = InsultBehavior()
        behavior.action("Mensaje")
        mock_chat.assert_called_with("InsultBot dice: Mensaje, pero en realidad, ¡eres una tortuga!")

    @patch("mcpi.minecraft.Minecraft.postToChat")
    @patch("mcpi.minecraft.Minecraft.setBlock")
    def test_tnt_behavior(self, mock_set_block, mock_chat):
        behavior = TNTBehavior()
        behavior.action("Explosión")
        mock_chat.assert_called_with("TNTBot ha recibido: Explosión")
        mock_set_block.assert_called()  # Verifica que se intenta colocar TNT

    @patch("mcpi.minecraft.Minecraft.postToChat")
    def test_move_behavior(self, mock_chat):
        behavior = MoveBehavior()
        behavior.action()
        mock_chat.assert_called_with("MoveBehavior: Agente movido a la posición (11, 5, 10)")

    @patch("mcpi.minecraft.Minecraft.postToChat")
    @patch("mcpi.minecraft.Minecraft.setBlock")
    def test_build_behavior(self, mock_set_block, mock_chat):
        behavior = BuildBehavior()
        behavior.action()
        mock_chat.assert_called_with("BuildBehavior: Torre de piedra construida.")
        self.assertEqual(mock_set_block.call_count, 5)  # Verificar que coloca 5 bloques

    @patch("mcpi.minecraft.Minecraft.postToChat")
    @patch("mcpi.minecraft.Minecraft.setBlock")
    def test_destroy_behavior(self, mock_set_block, mock_chat):
        behavior = DestroyBehavior()
        behavior.action()
        mock_chat.assert_called_with("DestroyBehavior: Bloque destruido.")
        mock_set_block.assert_called_once_with(8, 5, 10, 0)  # Verifica que destruye el bloque
