import unittest
import pygame
from car_game import PlayerVehicle

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_inicializacion_jugador(self):
        jugador = PlayerVehicle(250, 400)
        self.assertEqual(jugador.rect.center, (250, 400))

if __name__ == '__main__':
    unittest.main(verbosity=2)