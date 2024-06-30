import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()
            
    def test_aumento_velocidad_por_puntuacion(self):
        score = 0
        speed = 2
        
        # Simular aumento de puntuación
        for _ in range(10):
            score += 1
            if score > 0 and score % 5 == 0:
                speed += 1
        
        self.assertEqual(speed, 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)