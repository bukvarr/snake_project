import copy
import random

import Colors
import GameConstants
import SpeedConstants
import Util
import GameObjects
import levels

import pygame


class Map:
    snake = GameObjects.MovableObject(GameConstants.snake_start_pos, Colors.RED, SpeedConstants.forward_speed)
    coin = GameObjects.StaticObject(GameConstants.coin_start_pos, Colors.YELLOW)
    walls = []
    super_coin_spawned = False

    def restart(self):
        self.snake.update(GameConstants.snake_start_pos, Colors.RED, SpeedConstants.forward_speed)
        self.coin = GameObjects.StaticObject(GameConstants.coin_start_pos, Colors.YELLOW)
        self.walls.clear()
        self.super_coin_spawned = False

    def set_new_coin(self):
        vacant_positions = set()
        for i in range(GameConstants.WIDTH // GameConstants.object_size):
            for j in range(GameConstants.HEIGHT // GameConstants.object_size):
                vacant_positions.add((i * GameConstants.object_size, j * GameConstants.object_size))
        for point in self.snake.all_points:
            vacant_positions.remove((point.x, point. y))
        for wall in self.walls:
            vacant_positions.remove((wall.head_pos.x, wall.head_pos.y))
        new_pos = random.SystemRandom().sample(vacant_positions, 1)[0]
        self.coin.head_pos = Util.Point(new_pos[0], new_pos[1])
        if self.snake.size() % GameConstants.super_coin_spawn_rate == 0:
            self.super_coin_spawned = True
            self.coin.color = Colors.GREEN
        else:
            self.super_coin_spawned = False
            self.coin.color = Colors.YELLOW

    def set_border_walls(self):
        wall_color = Colors.GREY
        for i in range(GameConstants.WIDTH // GameConstants.object_size - 2):
            x = (i + 1) * GameConstants.object_size
            y = GameConstants.HEIGHT - GameConstants.object_size
            self.walls.append(GameObjects.StaticObject(Util.Point(x, y), wall_color))
            y = 0
            self.walls.append(GameObjects.StaticObject(Util.Point(x, y), wall_color))
        for i in range(GameConstants.HEIGHT // GameConstants.object_size - 2):
            y = (i + 1) * GameConstants.object_size
            x = GameConstants.WIDTH - GameConstants.object_size
            self.walls.append(GameObjects.StaticObject(Util.Point(x, y), wall_color))
            x = 0
            self.walls.append(GameObjects.StaticObject(Util.Point(x, y), wall_color))
        min_x = 0
        min_y = 0
        max_x = GameConstants.HEIGHT - GameConstants.object_size
        max_y = GameConstants.HEIGHT - GameConstants.object_size
        self.walls.append(GameObjects.StaticObject(Util.Point(min_x, min_y), wall_color))
        self.walls.append(GameObjects.StaticObject(Util.Point(min_x, max_y), wall_color))
        self.walls.append(GameObjects.StaticObject(Util.Point(max_x, min_y), wall_color))
        self.walls.append(GameObjects.StaticObject(Util.Point(max_x, max_y), wall_color))

    def set_additional_walls(self, lvl_num):
        wall_color = Colors.GREY
        if lvl_num == 1:
            return
        if lvl_num == 2:
            walls_pos = levels.Level(2)
            for pos in walls_pos.walls:
                self.walls.append(GameObjects.StaticObject(copy.copy(pos), wall_color))
        elif lvl_num == 3:
            walls_pos = levels.Level(3)
            for pos in walls_pos.walls:
                self.walls.append(GameObjects.StaticObject(copy.copy(pos), wall_color))
        elif lvl_num == 4:
            walls_pos = levels.Level(4)
            for pos in walls_pos.walls:
                self.walls.append(GameObjects.StaticObject(copy.copy(pos), wall_color))
        elif lvl_num == 5:
            walls_pos = levels.Level(5)
            for pos in walls_pos.walls:
                self.walls.append(GameObjects.StaticObject(copy.copy(pos), wall_color))
