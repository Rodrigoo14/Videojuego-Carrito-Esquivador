import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_movimiento_izquierda_jugador(self):
        jugador = PlayerVehicle(250, 400)
        jugador.rect.x -= 100
        self.assertEqual(jugador.rect.centerx, 150)


if __name__ == '__main__':
    unittest.main(verbosity=2)