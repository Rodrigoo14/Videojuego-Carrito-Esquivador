import unittest
import pygame
from car_game import Vehicle

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_movimiento_vehiculo(self):
        imagen = pygame.Surface((50, 100))
        vehiculo = Vehicle(imagen, 250, 0)  # Crear el vehículo en la posición inicial (250, 0)
        grupo_vehiculos = pygame.sprite.Group(vehiculo)
        
        # Simula el movimiento del vehículo hacia abajo
        for _ in range(10):
            vehiculo.rect.y += 1
            grupo_vehiculos.update()  # Actualiza el grupo de vehículos después de cada cambio de posición
        
        # Verifica que la posición y del rectángulo del vehículo sea 10 después de moverlo
        self.assertEqual(vehiculo.rect.y, 10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
