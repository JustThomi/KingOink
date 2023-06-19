import src.spritesheet as spritesheet


class Animation:
    def __init__(self, img, size, speed, loop=True) -> None:
        self.sprite_sheet = spritesheet.Spritesheet(img, size)
        self.width, self.height = size

        self.current_frame = 0
        self.frame = self.sprite_sheet.fetch_frame(self.current_frame)
        self.length = self.sprite_sheet.get_length()
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
        status = ''

        if self.current_frame == self.length:
            if not self.loop:
                status = 'done'
            else:
                self.current_frame = 0
        else:
            self.current_frame += 1

        return status

    def update(self):
        status = ''

        if self.time == self.speed:
            status = self.next_frame()
            self.frame = self.sprite_sheet.fetch_frame(self.current_frame)
            self.time = 0
        else:
            self.time += 1

        return status


class AnimationManager:
    def __init__(self, animations) -> None:
        self.animations = animations
        self.animation_status = ''
        self.state = 'idle'
        self.next_state = ''

    def set_state(self, state):
        if self.animations[self.state].loop:
            self.animation_status = ''
            self.state = state
        else:
            self.next_state = state

    def get_current_animation(self):
        return self.animations[self.state]

    def update(self):
        if self.animations[self.state].loop:
            self.animations[self.state].update()
        else:
            if self.animation_status == 'done':
                if self.next_state != '':
                    self.animations[self.state].reset()
                    self.state = self.next_state
                    self.next_state = ''
            else:
                self.animation_status = self.animations[self.state].update()
