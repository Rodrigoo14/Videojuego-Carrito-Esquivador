import unittest
import pygame
from car_game import Vehicle

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_incremento_puntaje(self):
        puntaje = 0
        vehiculo = Vehicle(pygame.Surface((50, 100)), 250, 499)  # Asegúrate de que el tamaño de la superficie sea correcto
        grupo_vehiculos = pygame.sprite.Group(vehiculo)
        
        # Simula que el vehículo sale de la pantalla
        for _ in range(10):
            vehiculo.rect.y += 1
            grupo_vehiculos.update()  # Actualiza el grupo después de cada movimiento

            if vehiculo.rect.top >= 500:
                vehiculo.kill()
                puntaje += 1
        
        self.assertEqual(puntaje, 1)
        self.assertEqual(len(grupo_vehiculos), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
