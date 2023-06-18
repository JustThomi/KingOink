import pygame
import src.scenes as scenes
import src.settings as settings


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.state = 'game'
        self.current_level = 0
        self.levels = [
            scenes.Level(
                screen, settings.tutorial_level, settings.tutorial_decore, True, self.next_level),
            scenes.Level(
                screen, settings.tutorial_level, settings.tutorial_decore, False, self.next_level)
        ]

        self.lose_scene = scenes.Lose()
        self.pause_scene = scenes.Pause()

    def render(self):
        self.screen.fill((63, 56, 81))

    def set_state(self, state):
        self.state = state

    def next_level(self):
        if self.current_level + 1 < len(self.levels):
            self.current_level += 1
        else:
            self.set_state('win')

    def update(self):
        match self.state:
            case 'game':
                self.render()
                self.levels[self.current_level].update()
            case 'lose':
                self.lose_scene.update()
            case 'pause':
                self.pause_scene.update()
            case 'win':
                self.pause_scene.update()


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
