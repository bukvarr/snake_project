import GameConstants
import Util

lvl5_walls_num = GameConstants.WIDTH // (5 * GameConstants.object_size) + 4
lvl5_start_x = GameConstants.HEIGHT // 5 - 3 * GameConstants.object_size
lvl5_start_y = GameConstants.WIDTH // 2 - lvl5_walls_num // 2 * GameConstants.object_size


class Level:
    walls = []

    def __init__(self, lvl_num):
        self.walls.clear()
        if lvl_num == 2:
            walls_num = GameConstants.WIDTH // (5 * GameConstants.object_size)
            start_x = GameConstants.WIDTH // 2 - walls_num // 2 * GameConstants.object_size
            y = GameConstants.HEIGHT - GameConstants.HEIGHT // 5 + GameConstants.object_size
            for i in range(walls_num):
                self.walls.append(Util.Point(start_x + i * GameConstants.object_size, y))
        if lvl_num == 3:
            walls_num = GameConstants.WIDTH // (5 * GameConstants.object_size)
            start_x = GameConstants.WIDTH // 2 - walls_num // 2 * GameConstants.object_size
            y = GameConstants.HEIGHT - GameConstants.HEIGHT // 5 + GameConstants.object_size
            for i in range(walls_num):
                if i % 2 == 0:
                    self.walls.append(Util.Point(start_x + i * GameConstants.object_size, y))
            y = GameConstants.HEIGHT // 5 - GameConstants.object_size
            for i in range(walls_num):
                if i % 2 == 0:
                    self.walls.append(Util.Point(start_x + i * GameConstants.object_size, y))
        if lvl_num == 4:
            walls_num = GameConstants.WIDTH // (5 * GameConstants.object_size)
            start_x = GameConstants.WIDTH // 2 - walls_num // 2 * GameConstants.object_size
            y = GameConstants.HEIGHT - GameConstants.HEIGHT // 5 + GameConstants.object_size
            for i in range(walls_num):
                self.walls.append(Util.Point(start_x + i * GameConstants.object_size, y))
            y = GameConstants.HEIGHT // 5 - GameConstants.object_size
            for i in range(walls_num):
                self.walls.append(Util.Point(start_x + i * GameConstants.object_size, y))

        if lvl_num == 5:
            walls_num = lvl5_walls_num
            start_y = lvl5_start_y
            start_x = lvl5_start_x
            row_num = (GameConstants.HEIGHT - 2 * start_x) // GameConstants.object_size + 3
            for j in range(row_num):
                if j % 5 == 0:
                    x = start_x + j * GameConstants.object_size
                    for i in range(walls_num):
                        self.walls.append(Util.Point(x, start_y + i * GameConstants.object_size))



