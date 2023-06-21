import pygame
import os
import src.spritesheet as spritesheet
import src.settings as settings
import src.entities as entities

# I should have made a parent class but oh well


class Win:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('assets', 'Monocraft.ttf'), 32)

        self.title = pygame.image.load(
            os.path.join('assets', 'pause_title.png'))
        self.title = pygame.transform.scale(
            self.title, (self.title.get_width() * 5, self.title.get_height() * 5))
        self.credits = self.font.render('made by WildDev using pygame-ce', False, (255, 255, 255))

        self.background = pygame.Surface(
            self.screen.get_size()).convert()
        self.background.set_alpha(100)
        self.background.fill((63, 56, 81, 50))

    def update(self):
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.credits, (self.screen.get_width() / 2 - self.unpause_hint.get_width() / 2, self.screen.get_height() / 2 + 100))
        self.screen.blit(self.title, (self.screen.get_width() /
                         2 - self.title.get_width() / 2, self.screen.get_height() / 2 - self.title.get_height() * 2))



class Lose:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('assets', 'Monocraft.ttf'), 32)

        self.title = pygame.image.load(
            os.path.join('assets', 'lose_title.png'))
        self.title = pygame.transform.scale(
            self.title, (self.title.get_width() * 5, self.title.get_height() * 5))
        self.hint = self.font.render('press esc to retry', False, (255, 255, 255))
        
        self.background = pygame.Surface(
            self.screen.get_size()).convert()
        self.background.set_alpha(100)
        self.background.fill((63, 56, 81))

    def update(self):
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, (self.screen.get_width() /
                         2 - self.title.get_width() / 2, self.screen.get_height() / 2 - self.title.get_height() * 2))


class Pause:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(os.path.join('assets', 'Monocraft.ttf'), 32)

        self.title = pygame.image.load(
            os.path.join('assets', 'pause_title.png'))
        self.title = pygame.transform.scale(
            self.title, (self.title.get_width() * 5, self.title.get_height() * 5))
        self.unpause_hint = self.font.render('press ESC to unpause', False, (255, 255, 255))

        self.background = pygame.Surface(
            self.screen.get_size()).convert()
        self.background.set_alpha(100)
        self.background.fill((63, 56, 81, 50))

    def update(self):
        self.render()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.unpause_hint, (self.screen.get_width() / 2 - self.unpause_hint.get_width() / 2, self.screen.get_height() / 2 + 100))
        self.screen.blit(self.title, (self.screen.get_width() /
                         2 - self.title.get_width() / 2, self.screen.get_height() / 2 - self.title.get_height() * 2))


class Level:
    def __init__(self, screen, layout, deco_layout, tutorial, swap_level, set_state) -> None:
        self.layout = layout
        self.deco_layout = deco_layout
        self.screen = screen
        self.is_tutorial = tutorial
        self.level_cleared = False
        self.swap_level = swap_level

        self.entities = []
        self.player = entities.Player(screen, set_state)
        self.entities.append(self.player)
        self.scroll_speed = 0
        self.player_vel = self.player.velocity

        self.terrain_tiles = spritesheet.TerrainTiles()
        self.decoratione_tiles = spritesheet.DecorationTiles()
        self.map = []
        self.collidables = []

        self.load()
        self.setup_level()
        if self.is_tutorial:
            self.setup_tutorial()

    def load(self):
        for row_id, row in enumerate(self.layout):
            for tile_id, tile in enumerate(row):
                if tile in self.terrain_tiles.background.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        self.terrain_tiles.background[tile], position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                elif tile in self.terrain_tiles.walls.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        self.terrain_tiles.walls[tile], position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                    self.collidables.append(t)

        for row_id, row in enumerate(self.deco_layout):
            for tile_id, tile in enumerate(row):
                if tile in self.decoratione_tiles.decorations.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        self.decoratione_tiles.decorations[tile], position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                if tile in self.decoratione_tiles.platforms.keys():
                    position = (tile_id * settings.tile_size,
                                row_id * settings.tile_size)
                    t = spritesheet.Tile(
                        self.decoratione_tiles.platforms[tile], position, (settings.tile_size, settings.tile_size))
                    self.map.append(t)
                    self.collidables.append(t)

    def setup_tutorial(self):
        self.title = pygame.image.load(
            os.path.join('assets', 'KingOink_title.png'))
        self.title = pygame.transform.scale(
            self.title, (self.title.get_width() * 4, self.title.get_height() * 4))

        self.a_key = spritesheet.Tile(
            self.decoratione_tiles.hints['L'], (600, 400), self.decoratione_tiles.hints['L'].get_size())
        self.d_key = spritesheet.Tile(
            self.decoratione_tiles.hints['R'], (680, 400), self.decoratione_tiles.hints['R'].get_size())
        self.w_key = spritesheet.Tile(
            self.decoratione_tiles.hints['J'], (640, 350), self.decoratione_tiles.hints['J'].get_size())
        self.space_key = spritesheet.Tile(
            self.decoratione_tiles.hints['A'], (1000, 400), self.decoratione_tiles.hints['A'].get_size())

        self.map.append(self.a_key)
        self.map.append(self.d_key)
        self.map.append(self.w_key)
        self.map.append(self.space_key)

    def setup_level(self):
        self.enter_door = entities.Door('enter', self.screen, (500, 400))
        self.exit_door = entities.Door(
            'exit', self.screen, (2100, 400), self.swap_level)
        self.box = entities.Box(self.screen, (600, 480))

        self.map.append(self.enter_door)
        self.map.append(self.exit_door)

        # box collide test
        self.map.append(self.box)
        self.collidables.append(self.box)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.player.direction.x = -1
            self.player.flip_sprite = True
            self.player.animation_manager.set_state('run')
        elif keys[pygame.K_d]:
            self.player.direction.x = 1
            self.player.flip_sprite = False
            self.player.animation_manager.set_state('run')
        else:
            self.player.direction.x = 0
            self.player.animation_manager.set_state('idle')

        if keys[pygame.K_w]:
            if not self.player.is_in_air:
                self.player.jump()

        if keys[pygame.K_SPACE]:
            self.player.attack()

        if keys[pygame.K_RETURN] and self.player.rect.colliderect(self.exit_door.rect):
            if not self.level_cleared:
                self.exit_door.animation_manager.set_state('open')
                self.level_cleared = not self.level_cleared

    def vertical_collision(self):
        for entity in self.entities:
            entity.gravity()

            for tile in self.collidables:
                if tile.rect.colliderect(entity.rect):
                    if entity.direction.y > 0:
                        entity.rect.bottom = tile.rect.top
                        entity.direction.y = 0
                        entity.is_in_air = False
                    if entity.direction.y < 0:
                        entity.rect.top = tile.rect.bottom
                        entity.direction.y = 0

    def horizontal_collision(self):
        for entity in self.entities:
            for tile in self.collidables:
                if tile.rect.colliderect(entity.rect):
                    if entity.direction.x > 0:
                        entity.rect.right = tile.rect.left
                    if entity.direction.x < 0:
                        entity.rect.left = tile.rect.right

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

    def show_tutorial(self):
        self.screen.blit(self.title, (self.screen.get_width() /
                                      2 - self.title.get_width()/2, 200))

    def update(self):
        self.render()
        self.scroll_map()
        self.input()
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()

        self.box.update()
        self.enter_door.update()
        self.exit_door.update()

    def render(self):
        # render tiles
        for tile in self.map:
            tile.surface.set_colorkey((0, 0, 0))
            self.screen.blit(tile.surface, tile.rect)

        if self.is_tutorial:
            self.show_tutorial()

        self.enter_door.render()
        self.exit_door.render()
        self.box.render()
        self.player.render()
