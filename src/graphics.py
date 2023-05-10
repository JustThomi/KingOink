import pygame


class Animation:
    def __init__(self, spritesheet, size, speed) -> None:
        self.sprite_sheet = spritesheet
        self.width, self.height = size

        self.frame = pygame.Surface(size).convert_alpha()
        self.length = (self.sprite_sheet.get_width() / self.width) - 1
        self.current_frame = 0
        self.time = 0
        self.speed = speed

        self.fetch_frame()

    def get_frame(self):
        return self.frame

    def fetch_frame(self):
        self.frame = pygame.Surface(
            (self.width, self.height)).convert_alpha()
        self.frame.blit(self.sprite_sheet, (0, 0),
                        (self.width * self.current_frame, 0, self.width, self.height))
        self.frame = pygame.transform.scale(
            self.frame, (self.width * 3, self.height * 3))

    def next_frame(self):
        if self.current_frame == self.length:
            self.current_frame = 0
        else:
            self.current_frame += 1

    def update(self):
        if self.time == self.speed:
            self.next_frame()
            self.fetch_frame()
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
