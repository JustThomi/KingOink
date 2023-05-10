import pygame
import os
import src.graphics as graphics


class Player:
    def __init__(self, screen):
        self.health = 100
        self.velocity = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_force = -20
        self.is_in_air = False

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
        if self.is_in_air:
            self.gravity()
        self.input()
        self.move()
        self.animation_manager.update()
        self.animate()
        self.render()

    def render(self):
        # load and set correct direction of frame
        self.surface = self.animation_manager.get_current_animation().get_frame()

        if self.flip_sprite:
            self.surface = pygame.transform.flip(self.surface, True, False)

        self.surface.set_colorkey((0, 0, 0))
        self.screen.blit(self.surface, (self.rect.x, self.rect.y))

    def gravity(self):
        # TODO move gravity to Game() to affect all entities (when they'll be implemented)
        # temp solution to stop player from falling forever
        # will fix when I implement some ground and collision
        if self.direction.y < 20 and self.is_in_air:
            self.direction.y += 0.9  # g force
        else:
            self.is_in_air = False
            self.direction.y = 0

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

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.flip_sprite = True
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.flip_sprite = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if not self.is_in_air:
                self.jump()
