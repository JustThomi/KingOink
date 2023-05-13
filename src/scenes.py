import pygame
import src.spritesheet as spritesheet
import src.settings as settings

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

        self.terrain_tiles = spritesheet.TerrainTiles()
        self.bg_tiles = []
        self.wall_tiles = []

        self.load()

    def load(self):
        for row_id, row in enumerate(self.layout):
            for tile_id, tile in enumerate(row):
                if tile in self.terrain_tiles.background.keys():
                    position = (tile_id * settings.tile_size, row_id * settings.tile_size)
                    t = spritesheet.Tile(tile, position, (settings.tile_size, settings.tile_size))
                    self.bg_tiles.append(t)
                elif tile in self.terrain_tiles.walls.keys():
                    position = (tile_id * settings.tile_size, row_id * settings.tile_size)
                    t = spritesheet.Tile(tile, position, (settings.tile_size, settings.tile_size))
                    self.wall_tiles.append(t)

    def update(self):
        pass
    
    def render(self):
        # render tiles
        for tile in self.bg_tiles:
            self.screen.blit(self.terrain_tiles.background[tile.sprite_id], (tile.rect.x, tile.rect.y))

        for tile in self.wall_tiles:
            self.screen.blit(self.terrain_tiles.walls[tile.sprite_id], (tile.rect.x, tile.rect.y))