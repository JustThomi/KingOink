import pygame
import src.scenes as scenes
import src.settings as settings


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.state = 'tutorial'

        # scenes
        self.lose_scene = scenes.Lose()
        self.pause_scene = scenes.Pause()
        self.tutorial = scenes.Level(screen, settings.menu_level, True)
        self.level = scenes.Level(screen, settings.menu_level, False)

    def render(self):
        self.screen.fill((63, 56, 81))

    def set_state(self, state):
        self.state = state

    def update(self):
        match self.state:
            case 'game':
                self.render()
                self.level.update()
            case 'lose':
                self.render()
                self.lose_scene.update()
            case 'tutorial':
                self.render()
                self.tutorial.update()


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
