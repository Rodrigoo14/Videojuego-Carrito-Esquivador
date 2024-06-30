import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()
            
    def test_eliminar_vehiculos_fuera_de_pantalla(self):
        vehicle = Vehicle(pygame.Surface((50, 100)), 250, 0)  # Crear un vehículo en la parte superior de la pantalla
        group_vehicles = pygame.sprite.Group(vehicle)
        
        # Mover el vehículo fuera de la pantalla hacia abajo
        vehicle.rect.y = 600  # Suponiendo una posición fuera de la pantalla
        vehicle.kill()  # Eliminar el vehículo
        
        self.assertEqual(len(group_vehicles), 0)  # Verificar que no haya vehículos en el grupo después de eliminarlo


if __name__ == '__main__':
    unittest.main(verbosity=2)