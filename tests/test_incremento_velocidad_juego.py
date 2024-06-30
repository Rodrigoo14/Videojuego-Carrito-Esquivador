import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes, main

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_incremento_velocidad_juego(self):
        velocidad = 2
        puntaje = 0
        grupo_vehiculos = pygame.sprite.Group()
        
        for _ in range(6):
            puntaje += 1
            if puntaje > 0 and puntaje % 5 == 0:
                velocidad += 1
        
        self.assertEqual(velocidad, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)