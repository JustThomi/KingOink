import src.graphics as graphics
import pygame
import os


class Heart:
    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.width, self.height = 18, 14
        self.rect = pygame.Rect(pos, (self.width, self.height))
        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'lives_coins', 'heart_idle.png')).convert_alpha(), (self.width, self.height), 5),
            'hit': graphics.Animation(pygame.image.load(os.path.join('assets', 'lives_coins', 'heart_hit.png')).convert_alpha(), (self.width, self.height), 5, False),
        }

        self.animation_manager = graphics.AnimationManager(self.animations)

        self.remove = False

    def update(self):
        self.animation_manager.update()
        if self.animation_manager.state == 'hit':
            self.remove = True
        self.render()

    def render(self):
        self.surface = self.animation_manager.get_current_animation().get_frame()
        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))


class Healthbar:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.width, self.height = 66, 34
        self.y_pos = self.screen.get_height() - self.height - 100
        self.rect = pygame.Rect(100, self.y_pos, self.width, self.height)
        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'lives_coins', 'health_bar.png')).convert_alpha(), (self.width, self.height), 1)
        }

        self.animation_manager = graphics.AnimationManager(self.animations)

        self.lives = [
            Heart(self.screen, (166, self.y_pos + 20)),
            Heart(self.screen, (144, self.y_pos + 20)),
            Heart(self.screen, (122, self.y_pos + 20)),
        ]

    def took_damage(self):
        if len(self.lives) > 0:
            self.lives[0].animation_manager.set_state('hit')

    def render(self):
        self.surface = self.animation_manager.get_current_animation().get_frame()
        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def update(self):
        self.animation_manager.update()
        for l in self.lives:
            l.update()
        if self.lives[0].remove:
            self.lives.pop(0)
