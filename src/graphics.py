import pygame
import src.spritesheet as spritesheet


class Animation:
    def __init__(self, img, size, speed, loop=True) -> None:
        self.sprite_sheet = spritesheet.Spritesheet(img, size)
        self.width, self.height = size

        self.current_frame = 0
        self.frame = self.sprite_sheet.fetch_frame(self.current_frame)
        self.length = self.sprite_sheet.get_lenght()
        self.time = 0
        self.speed = speed
        self.loop = loop

    def get_frame(self):
        return self.frame

    def reset(self):
        self.current_frame = 0
        self.time = 0
        self.frame = self.sprite_sheet.fetch_frame(self.current_frame)

    def next_frame(self):
        if self.current_frame == self.length:
            if not self.loop:
                return 'done'
            else:
                self.current_frame = 0
        else:
            self.current_frame += 1

        return ''

    def update(self):
        status = ''

        if self.time == self.speed:
            status = self.next_frame()
            self.frame = self.sprite_sheet.fetch_frame(
                self.current_frame)
            self.time = 0
        else:
            self.time += 1

        return status


class AnimationManager:
    def __init__(self, animations) -> None:
        self.animations = animations
        self.animation_state = ''
        self.state = 'idle'

    def set_state(self, state):
        self.animation_state = ''
        self.state = state

    def get_current_animation(self):
        return self.animations[self.state]

    def update(self):
        if self.animations[self.state].loop:
            self.animations[self.state].update()
        elif self.animation_state != 'done':
            self.animation_state = self.animations[self.state].update()

