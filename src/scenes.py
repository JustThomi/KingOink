import pygame
import src.spritesheet as spritesheet
import src.settings as settings
import src.player as player


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
    def __init__(self, screen, layout) -> None:
        self.layout = layout
        self.screen = screen

        self.player = player.Player(screen)
        self.scroll_speed = 0
        self.player_vel = self.player.velocity

        self.terrain_tiles = spritesheet.TerrainTiles()
        self.map = []
        self.bg_tiles = []
        self.wall_tiles = []

        self.load()

    def load(self):
        for row_id, row in enumerate(self.layout):
            for tile_id, tile in enumerate(row):
                if tile in self.terrain_tiles.background.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        tile, position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                    self.bg_tiles.append(t)
                elif tile in self.terrain_tiles.walls.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        tile, position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                    self.wall_tiles.append(t)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.player.direction.x = -1
            self.player.flip_sprite = True
        elif keys[pygame.K_d]:
            self.player.direction.x = 1
            self.player.flip_sprite = False
        else:
            self.player.direction.x = 0

        if keys[pygame.K_SPACE]:
            if not self.player.is_in_air:
                self.player.jump()

    def vertical_collision(self):
        self.player.gravity()

        for tile in self.wall_tiles:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.rect.bottom = tile.rect.top
                    self.player.direction.y = 0
                    self.player.is_in_air = False
                if self.player.direction.y < 0:
                    self.player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0

    def horizontal_collision(self):
        for tile in self.wall_tiles:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.x > 0:
                    self.player.rect.right = tile.rect.left
                if self.player.direction.x < 0:
                    self.player.rect.left = tile.rect.right

    def update(self):
        self.scroll_map()
        self.input()
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()

    def move_map(self):
        for tile in self.map:
            tile.rect.x += self.scroll_speed

    def scroll_map(self):
        self.move_map()

        if self.player.rect.x > self.screen.get_width()/2 + 100 and self.player.direction.x > 0:
            self.scroll_speed = -self.player_vel
            self.player.velocity = 0
        elif self.player.rect.x < self.screen.get_width()/2 - 200 and self.player.direction.x < 0:
            self.player.velocity = 0
            self.scroll_speed = self.player_vel
        else:
            self.scroll_speed = 0
            self.player.velocity = self.player_vel

    def render(self):
        # render tiles
        for tile in self.bg_tiles:
            self.screen.blit(
                self.terrain_tiles.background[tile.sprite_id], (tile.rect.x, tile.rect.y))

        for tile in self.wall_tiles:
            self.screen.blit(
                self.terrain_tiles.walls[tile.sprite_id], tile.rect)

        self.player.render()
