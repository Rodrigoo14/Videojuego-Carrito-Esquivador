import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_eliminacion_vehiculo_fuera_pantalla(self):
        imagen = pygame.Surface((50, 100))
        vehiculo = Vehicle(imagen, 250, 495)
        grupo_vehiculos = pygame.sprite.Group(vehiculo)
        
        # Simula que el vehículo se mueve fuera de la pantalla
        for _ in range(10):
            vehiculo.rect.y += 1
            if vehiculo.rect.top >= 500:
                grupo_vehiculos.remove(vehiculo)
        
        self.assertEqual(len(grupo_vehiculos), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)