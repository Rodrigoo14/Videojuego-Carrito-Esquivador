import unittest
import pygame
from car_game import Vehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_no_superposicion_vehiculos(self):
        grupo_vehiculos = pygame.sprite.Group()

        # Crea y añade dos vehículos al mismo carril
        imagen = pygame.Surface((50, 100))
        vehiculo1 = Vehicle(imagen, lanes[0], 0)
        vehiculo2 = Vehicle(imagen, lanes[0], -150)
        grupo_vehiculos.add(vehiculo1)
        grupo_vehiculos.add(vehiculo2)

        # Asegura que los vehículos no se superpongan
        for vehiculo in grupo_vehiculos:
            for otro_vehiculo in grupo_vehiculos:
                if vehiculo != otro_vehiculo:
                    self.assertFalse(pygame.sprite.collide_rect(vehiculo, otro_vehiculo))

if __name__ == '__main__':
    unittest.main(verbosity=2)
