import pygame
import src.spritesheet as spritesheet


class Animation:
    def __init__(self, img, size, speed) -> None:
        self.sprite_sheet = spritesheet.Spritesheet(img, size)
        self.width, self.height = size

        self.current_frame = 0
        self.frame = self.sprite_sheet.fetch_frame(self.current_frame)
        self.length = self.sprite_sheet.get_lenght()
        self.time = 0
        self.speed = speed

    def get_frame(self):
        return self.frame

    def next_frame(self):
        if self.current_frame == self.length:
            self.current_frame = 0
        else:
            self.current_frame += 1

    def update(self):
        if self.time == self.speed:
            self.next_frame()
            self.frame = self.sprite_sheet.fetch_frame(
                self.current_frame)
            self.time = 0
        else:
            self.time += 1


class AnimationManager:
    def __init__(self, animations) -> None:
        self.animations = animations
        self.state = 'idle'

    def set_state(self, state):
        self.state = state

    def get_current_animation(self):
        return self.animations[self.state]

    def update(self):
        self.animations[self.state].update()
