import unittest
import pygame
from car_game import Vehicle, PlayerVehicle, lanes

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

    def tearDown(self):
        pygame.quit()

    def test_carga_imagenes_vehiculo(self):
        # Verifica que todas las imágenes de los vehículos se carguen correctamente
        nombres_imagenes = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
        for nombre_imagen in nombres_imagenes:
            try:
                imagen = pygame.image.load('images/' + nombre_imagen)
                self.assertIsNotNone(imagen)
            except pygame.error:
                self.fail(f"Fallo al cargar la imagen: {nombre_imagen}")

if __name__ == '__main__':
    unittest.main(verbosity=2)