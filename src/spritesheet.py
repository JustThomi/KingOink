import pygame
import src.graphics as graphics
import os


class Spritesheet:
    def __init__(self, image, size) -> None:
        self.sheet = image
        self.frame = pygame.Surface(size)
        self.width, self.height = size
        self.length = (self.sheet.get_width() / self.width) - 1

    def get_lenght(self):
        return self.length

    def fetch_frame(self, current_frame, row=0, scale=2):
        self.frame = pygame.Surface(
            (self.width, self.height)).convert_alpha()
        self.frame.blit(self.sheet, (0, 0),
                        (self.width * current_frame, self.height * row, self.width, self.height))
        self.frame = pygame.transform.scale(
            self.frame, (self.width * scale, self.height * scale))

        return self.frame


class Tile():
    def __init__(self, id, pos, size):
        self.sprite_id = id
        self.rect = pygame.Rect(pos, size)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


# generating levels from a list of strings
# might change this to images if it seems worth it
# or find something that's way better...
class TerrainTiles:
    def __init__(self) -> None:
        self.background_tileset = Spritesheet(pygame.image.load(
            os.path.join('assets', 'environment', 'terrain.png')), (32, 32))

        self.background = {
            'A': self.background_tileset.fetch_frame(1, 7),
            'B': self.background_tileset.fetch_frame(2, 7),
            'C': self.background_tileset.fetch_frame(3, 7),
            'D': self.background_tileset.fetch_frame(1, 8),
            'E': self.background_tileset.fetch_frame(2, 8),
            'F': self.background_tileset.fetch_frame(3, 8),
            'G': self.background_tileset.fetch_frame(1, 9),
            'H': self.background_tileset.fetch_frame(2, 9),
            'I': self.background_tileset.fetch_frame(3, 9),
        }

        self.walls = {
            'J': self.background_tileset.fetch_frame(1, 1),
            'K': self.background_tileset.fetch_frame(2, 1),
            'L': self.background_tileset.fetch_frame(3, 1),
            'M': self.background_tileset.fetch_frame(1, 2),
            'N': self.background_tileset.fetch_frame(3, 2),
            'O': self.background_tileset.fetch_frame(1, 3),
            'P': self.background_tileset.fetch_frame(2, 3),
            'Q': self.background_tileset.fetch_frame(3, 3),

            'R': self.background_tileset.fetch_frame(7, 1),
            'S': self.background_tileset.fetch_frame(8, 1),
            'T': self.background_tileset.fetch_frame(7, 2),
            'U': self.background_tileset.fetch_frame(8, 2),

            'V' : self.background_tileset.fetch_frame(5, 1),
            'W' : self.background_tileset.fetch_frame(5, 2),
            'X' : self.background_tileset.fetch_frame(5, 3),

            'Y' : self.background_tileset.fetch_frame(11, 1),
            'Z' : self.background_tileset.fetch_frame(10, 2)
        }


class DecorationTiles:
    def __init__(self) -> None:
        self.decorations_tileset = Spritesheet(pygame.image.load(
            os.path.join('assets', 'environment', 'decorations.png')), (32, 32))

        self.decorations = {
            'W': self.decorations_tileset.fetch_frame(2, 3),
            'I': self.decorations_tileset.fetch_frame(3, 3),
            'N': self.decorations_tileset.fetch_frame(2, 4),
            'D': self.decorations_tileset.fetch_frame(3, 4),
        }

# reference for level building untill I take the time to make a better system
# A B C    V    J K L       R S
# D E F    W    M   N       T U
# G H I    X    O P Q
