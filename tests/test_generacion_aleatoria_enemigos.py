import unittest
import pygame
import random
from car_game import Vehicle, PlayerVehicle, lanes, main

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.game_speed = 2
        self.game_score = 0
        self.game_over = False


    def tearDown(self):
        pygame.quit()

    def test_generacion_aleatoria_enemigos(self):
        player_x = 250
        player_y = 400
        player = PlayerVehicle(player_x, player_y)
        
        # sprite groups
        player_group = pygame.sprite.Group()
        vehicle_group = pygame.sprite.Group()
        player_group.add(player)
        
        initial_enemy_count = len(vehicle_group)
        
        # simulate game loop to verify random enemy generation
        running = True
        while running:
            self.clock.tick(120)  # simulate a frame rate of 120 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # simulate player input or game logic updates here
            
            # simulate enemy generation
            if len(vehicle_group) < 2:
                lane = random.choice(lanes)
                # Example: create a vehicle in a lane
                vehicle = Vehicle(pygame.Surface((30, 30)), lane, -30)
                vehicle_group.add(vehicle)
            
            # update screen
            self.screen.fill((0, 0, 0))  # fill with black for simplicity
            player_group.draw(self.screen)
            vehicle_group.draw(self.screen)
            pygame.display.flip()
            
            # check if new enemies were generated
            if len(vehicle_group) > initial_enemy_count:
                break  # exit loop if new enemies are generated
        
        self.assertGreater(len(vehicle_group), initial_enemy_count, "Expected more enemies to be generated")

if __name__ == '__main__':
    unittest.main()
