import pygame
import os
import src.graphics as graphics


class Player:
    def __init__(self, screen):
        self.health = 100
        self.velocity = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_force = -20
        self.is_in_air = True

        self.screen = screen
        self.width, self.height = (78, 58)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.screen.get_width() / 2,
                                self.screen.get_height() / 2, self.width, self.height)

        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'idle.png')), (self.width, self.height), 5),
            'run': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'run.png')), (self.width, self.height), 7),
            'jump': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'jump.png')), (self.width, self.height), 1),
            'fall': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'fall.png')), (self.width, self.height), 1)
        }

        self.animation_manager = graphics.AnimationManager(self.animations)
        self.flip_sprite = False

    def update(self):
        self.move()
        self.animation_manager.update()
        self.animate()

    def render(self):
        # load and set correct direction of frame
        self.surface = self.animation_manager.get_current_animation().get_frame()

        if self.flip_sprite:
            self.surface = pygame.transform.flip(self.surface, True, False)

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x - 38, self.rect.y - 30))

        # testing rects
        # white = pygame.Surface((self.width, self.height))
        # pygame.draw.rect(white, (255, 255, 255), self.rect)
        # self.screen.blit(white, self.rect)

    def gravity(self):
        if self.is_in_air:
            self.direction.y += 0.9
            self.rect.y += self.direction.y

    def animate(self):
        if self.direction.x == 0:
            self.animation_manager.set_state('idle')
        if self.direction.x != 0:
            self.animation_manager.set_state('run')
        if self.direction.y < 0:
            self.animation_manager.set_state('jump')
        if self.direction.y > 0:
            self.animation_manager.set_state('fall')

    def jump(self):
        self.direction.y = self.jump_force
        self.is_in_air = True

    def move(self):
        self.rect.x += self.direction.x * self.velocity


class Door:
    def __init__(self, state, screen, pos) -> None:
        self.state = state
        self.screen = screen
        self.width, self.height = (46, 56)
        self.surface = pygame.Surface((self.width, self.height))
        # hardcoded pos for testing
        self.rect = pygame.Rect(pos, (self.width, self.height))

        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'idle.png')), (self.width, self.height), 1),
            'open': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'opening.png')), (self.width, self.height), 5),
            'close': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'closing.png')), (self.width, self.height), 5)
        }

        self.animation_manager = graphics.AnimationManager(self.animations)

    def update(self):
        self.animation_manager.update()
        self.animate()

    def render(self):
        self.surface = self.animation_manager.get_current_animation().get_frame()

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def animate(self):
        # temp var
        cond = False
        self.animation_manager.set_state('idle')

        if cond:
            self.animation_manager.set_state('open')
        if cond:
            self.animation_manager.set_state('jump')
