import pygame, sys
from settings import *
from player import USER

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('SpriteTest')
        self.player = USER(self.screen)
        self.player.animation_set()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BackGround)
            self.player.update()
            pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
