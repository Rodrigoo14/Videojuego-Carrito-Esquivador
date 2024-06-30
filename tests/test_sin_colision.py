import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_sin_colision(self):
        jugador = PlayerVehicle(250, 400)
        imagen = pygame.Surface((50, 100))
        vehiculo = Vehicle(imagen, 250, 0)

        colision = pygame.sprite.collide_rect(jugador, vehiculo)
        self.assertFalse(colision)

if __name__ == '__main__':
    unittest.main(verbosity=2)