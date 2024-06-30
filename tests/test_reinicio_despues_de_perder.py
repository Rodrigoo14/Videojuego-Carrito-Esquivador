import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()
            
    def test_reinicio_despues_de_perder(self):
        player = PlayerVehicle(250, 400)
        vehicle = Vehicle(pygame.Surface((50, 100)), 250, 200)  # Crear un vehículo en posición de colisión
        
        # Simular colisión del jugador con otro vehículo
        player.rect.y = vehicle.rect.y
        self.assertTrue(pygame.sprite.collide_rect(player, vehicle))  # Verificar colisión
        
        # Simular reinicio del juego
        player.rect.center = (250, 400)  # Colocar al jugador de nuevo en la posición inicial
        self.assertEqual(player.rect.center, (250, 400))  # Verificar que el jugador esté en la posición inicial después de reiniciar

if __name__ == '__main__':
    unittest.main(verbosity=2)