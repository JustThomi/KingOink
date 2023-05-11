import pygame

class Spritesheet:
    def __init__(self, image, size) -> None:
        self.sheet = image
        self.frame = pygame.Surface(size)
        self.width, self.height = size
        self.length = (self.sheet.get_width() / self.width) - 1
    
    def get_lenght(self):
        return self.length

    def fetch_frame(self, current_frame):
        self.frame = pygame.Surface(
            (self.width, self.height)).convert_alpha()
        self.frame.blit(self.sheet, (0, 0),
                        (self.width * current_frame, 0, self.width, self.height))
        self.frame = pygame.transform.scale(
            self.frame, (self.width * 2, self.height * 2))

        return self.frame
