import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_colision_vehiculos_lateral(self):
        player = PlayerVehicle(250, 400)
        vehicle = Vehicle(pygame.Surface((50, 100)), 250, 200)
        
        # Verificar que no haya colisión inicialmente
        self.assertFalse(pygame.sprite.collide_rect(player, vehicle))
        
        # Mover el jugador hacia la posición del vehículo
        player.rect.y = vehicle.rect.y
        self.assertTrue(pygame.sprite.collide_rect(player, vehicle))

if __name__ == '__main__':
    unittest.main(verbosity=2)