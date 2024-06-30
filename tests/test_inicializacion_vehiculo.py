import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_inicializacion_vehiculo(self):
        imagen = pygame.Surface((50, 100))
        vehiculo = Vehicle(imagen, 250, 0)
        self.assertEqual(vehiculo.rect.center, (250, 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)