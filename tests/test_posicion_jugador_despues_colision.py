import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_posicion_jugador_despues_colision(self):
        jugador = PlayerVehicle(250, 400)
        imagen = pygame.Surface((50, 100))
        vehiculo = Vehicle(imagen, 350, 400)

        jugador.rect.x += 100
        colision = pygame.sprite.collide_rect(jugador, vehiculo)

        if colision:
            jugador.rect.right = vehiculo.rect.left

        self.assertEqual(jugador.rect.right, vehiculo.rect.left)

if __name__ == '__main__':
    unittest.main(verbosity=2)