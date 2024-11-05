import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()


if __name__ == "__main__":
    unittest.main()