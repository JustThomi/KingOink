import pygame
import src.settings as settings
import src.graphics as graphics

class Menu:
    def __init__(self) -> None:
        pass

    def update(self):
        pass
    
    def render(self):
        pass

class Lose:
    def __init__(self) -> None:
        pass

    def update(self):
        pass
    
    def render(self):
        pass

class Pause:
    def __init__(self) -> None:
        pass 

    def update(self):
        pass
    
    def render(self):
        pass

class Level:
    def __init__(self, screen) -> None:
        self.layout = settings.level_1
        self.screen = screen
        self.tiles = []
        self.offset = pygame.Vector2(0, 0)

        self.load()

    def load(self):
        for row_id, row in enumerate(self.layout):
            for tile_id, tile in enumerate(row):
                if tile == 'X':
                    x, y = (tile_id + self.offset.x, row_id + self.offset.y)
                    t = graphics.Tile((x * settings.tile_size, y * settings.tile_size), settings.tile_size)
                    self.tiles.append(t)
    
    def update(self):
        pass
    
    def render(self):
        # render tiles
        for tile in self.tiles:
            self.screen.blit(tile.image, (tile.rect.x, tile.rect.y))