import pygame
import os

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = (58, 78)
        self.surface = pygame.Surface((self.width(), self.height())).convert_alpha()
        self.rect = self.surface.get_rect()
    
    def update(self):
        self.render()

    def render(self):
        pass