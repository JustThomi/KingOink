import pygame
import os
import src.graphics as graphics


class Player:
    def __init__(self, screen):
        self.health = 100
        self.velocity = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_force = -18
        self.is_in_air = True

        self.screen = screen
        self.width, self.height = (78, 58)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.screen.get_width() / 2,
                                self.screen.get_height() / 2, self.width - 25, self.height - 10)

        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'idle.png')), (self.width, self.height), 5),
            'run': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'run.png')), (self.width, self.height), 7),
            'jump': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'jump.png')), (self.width, self.height), 1),
            'fall': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'fall.png')), (self.width, self.height), 1),
            'attack': graphics.Animation(pygame.image.load(os.path.join('assets', 'player', 'attack.png')), (self.width, self.height), 5, False)
        }

        self.animation_manager = graphics.AnimationManager(self.animations)
        self.flip_sprite = False

    def update(self):
        self.move()
        self.animation_manager.update()

    def render(self):
        # load and set correct direction of frame
        self.surface = self.animation_manager.get_current_animation().get_frame()

        if self.flip_sprite:
            self.surface = pygame.transform.flip(self.surface, True, False)

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x - 50, self.rect.y - 40))

        # testing rects
        # white = pygame.Surface((self.rect.width, self.rect.height))
        # pygame.draw.rect(white, (255, 255, 255), self.rect)
        # self.screen.blit(white, self.rect)

    def gravity(self):
        self.direction.y += 0.9
        self.rect.y += self.direction.y

    def jump(self):
        self.animation_manager.set_state('jump')
        self.direction.y = self.jump_force
        self.is_in_air = True

    def attack(self):
        self.animation_manager.set_state('attack')

    def move(self):
        self.rect.x += self.direction.x * self.velocity


class Door:
    def __init__(self, state, screen, pos, change_scene = None) -> None:
        self.state = state
        self.screen = screen
        self.width, self.height = (46, 56)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(pos, (self.width * 2, self.height * 2))
        self.change_scene = change_scene

        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'idle.png')), (self.width, self.height), 1),
            'open': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'opening.png')), (self.width, self.height), 5, False),
            'close': graphics.Animation(pygame.image.load(os.path.join('assets', 'door', 'closing.png')), (self.width, self.height), 5, False)
        }

        self.animation_manager = graphics.AnimationManager(self.animations)

    def check_enter(self):
        if self.animation_manager.state == 'open' and self.animation_manager.animation_status == 'done':
            self.change_scene()

    def update(self):
        self.animate()

        if self.state == 'exit':
            self.check_enter()

    def render(self):
        self.surface = self.animation_manager.get_current_animation().get_frame()

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def animate(self):
        self.animation_manager.update()


class Box:
    def __init__(self, screen, position) -> None:
        self.screen = screen
        self.width, self.height = (22, 16)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.set_position(position)

        self.animations = {
            'idle': graphics.Animation(pygame.image.load(os.path.join('assets', 'box', 'idle.png')), (self.width, self.height), 1),
            'hit': graphics.Animation(pygame.image.load(os.path.join('assets', 'box', 'hit.png')), (self.width, self.height), 1),
        }
        self.animation_manager = graphics.AnimationManager(self.animations)

    def set_position(self, position):
        self.rect.x, self.rect.y = position

    def render(self):
        self.surface = self.animation_manager.get_current_animation().get_frame()

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def update(self):
        self.animation_manager.update()
        self.animate()

    def animate(self):
        self.animation_manager.set_state('idle')
