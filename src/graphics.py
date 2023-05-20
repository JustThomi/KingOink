import pygame
import src.spritesheet as spritesheet


class Animation:
    def __init__(self, img, size, speed, loop = True) -> None:
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
                self.reset()
                return 'done'
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
        self.state = 'idle'
        self.previous_state = ''

    def set_state(self, state):
        self.previous_state = self.state
        self.state = state

    def get_current_animation(self):
        return self.animations[self.state]

    def update(self):
        animation_status = self.animations[self.state].update()
        if animation_status == 'done':
            self.set_state(self.previous_state)