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
                screen, settings.tutorial_level, settings.tutorial_decore, True, self.next_level, self.set_state),
            scenes.Level(
                screen, settings.level_1, settings.level_1_decore, False, self.next_level, self.set_state),
            scenes.Level(
                screen, settings.level_2, settings.level_2_decore, False, self.next_level, self.set_state),
            scenes.Level(
                screen, settings.level_3, settings.level_3_decore, False, self.next_level, self.set_state),
            scenes.Level(
                screen, settings.level_4, settings.level_4_decore, False, self.next_level, self.set_state),
            scenes.Level(
                screen, settings.level_5, settings.level_5_decore, False, self.next_level, self.set_state),
        ]

        self.lose_scene = scenes.Lose(screen, self)
        self.pause_scene = scenes.Pause(screen)
        self.win_scene = scenes.Win(screen)

    def render(self):
        self.screen.fill((63, 56, 81))

    def set_state(self, state):
        self.state = state

    def pause(self):
        if self.state == 'game':
            self.set_state('pause')
        else:
            self.set_state('game')

    # not a good solutionw
    def reset_levels(self):
        self.levels = [
            scenes.Level(
                self.screen, settings.tutorial_level, settings.tutorial_decore, True, self.next_level, self.set_state),
            scenes.Level(
                self.screen, settings.level_1, settings.level_1_decore, False, self.next_level, self.set_state),
            scenes.Level(
                self.screen, settings.level_2, settings.level_2_decore, False, self.next_level, self.set_state),
            scenes.Level(
                self.screen, settings.level_3, settings.level_3_decore, False, self.next_level, self.set_state),
            scenes.Level(
                self.screen, settings.level_4, settings.level_4_decore, False, self.next_level, self.set_state),
            scenes.Level(
                self.screen, settings.level_5, settings.level_5_decore, False, self.next_level, self.set_state),
        ]

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
                self.win_scene.update()


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('King Oink')

    screen_height, screen_width = (1280, 720)
    screen = pygame.display.set_mode((screen_height, screen_width))

    clock = pygame.time.Clock()
    game = Game(screen)

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if game.state == 'win':
                        exit()
                    else:
                        game.pause()

        game.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
