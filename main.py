import pygame
import src.scenes as scenes
import src.settings as settings
import sys


class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.state = 'game'
        self.current_level = 0
        self.level = scenes.Level(
            screen, self.next_level, self.set_state, self.current_level)

        self.lose_scene = scenes.Lose(screen, self.reset_level, self.set_state)
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

    def reset_level(self):
        self.level = scenes.Level(
            self.screen, self.next_level, self.set_state, self.current_level)

    def next_level(self):
        if self.current_level + 1 < 5:
            self.current_level += 1
            self.reset_level()
        else:
            self.set_state('win')

    def update(self):
        match self.state:
            case 'game':
                self.render()
                self.level.update()
            case 'lose':
                self.lose_scene.update()
            case 'pause':
                self.pause_scene.update()
            case 'win':
                self.win_scene.update()


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption('King Oink')

    screen_height, screen_width = (1280, 720)
    screen = pygame.display.set_mode((screen_height, screen_width))

    clock = pygame.time.Clock()
    game = Game(screen)

    pygame.mixer.music.load("assets\sounds\music.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if game.state == 'win':
                        sys.exit()
                    else:
                        game.pause()

        game.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
