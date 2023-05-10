import pygame
import src.player as player


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.player = player.Player(self.screen)
        self.state = 'game'

    def render(self):
        self.screen.fill((57, 56, 82))

    def set_state(self, state):
        self.state = state

    def update(self):
        match self.state:
            case 'game':
                self.render()
                self.player.update()
            case 'lose':
                pass
            case 'levels':
                pass


def main():
    pygame.init()
    pygame.display.set_caption('Kings')

    screen_height, screen_width = (1280, 720)
    screen = pygame.display.set_mode((screen_height, screen_width))

    clock = pygame.time.Clock()
    game = Game(screen)

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        game.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
