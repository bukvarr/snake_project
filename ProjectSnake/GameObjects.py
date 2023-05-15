import GameConstants
import Util
import Colors
import SpeedConstants
import pygame
import collections
import copy


class GameObject():

    head_pos = Util.Point(0, 0)
    color = Colors.WHITE

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GameConstants.object_size, GameConstants.object_size))
        self.image.fill(Colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (GameConstants.snake_start_pos.x, GameConstants.snake_start_pos.y)

    def intersects_with(self, other):
        return self.head_pos.x == other.head_pos.x and self.head_pos.y == other.head_pos.y


class StaticObject(GameObject):

    def __init__(self, pos, color):
        self.head_pos = pos
        self.color = color
        pygame.sprite.Sprite.__init__(self)


class MovableObject(GameObject):

    speed = SpeedConstants.forward_speed
    all_points = collections.deque()
    buffed = False
    deleted_part = Util.Point(1, 1)

    def intersects_itself(self):
        for i in range(1, len(self.all_points)):
            if self.head_pos.x == self.all_points[i].x and self.head_pos.y == self.all_points[i].y:
                return True
        return False

    def __init__(self, pos, color, speed):
        self.head_pos = copy.copy(pos)
        self.color = color
        self.speed = speed
        self.all_points.append(Util.Point(self.head_pos.x, self.head_pos.y))

    def update(self, pos, color, speed):
        self.head_pos = copy.copy(pos)
        self.color = color
        self.speed = speed
        self.all_points.clear()
        self.all_points.append(Util.Point(self.head_pos.x, self.head_pos.y))
        self.buffed = False

    def move_tail(self):
        if self.buffed:
            self.buffed = False
        else:
            self.deleted_part = self.all_points.pop()
        #self.head_pos.move(self.speed)
        #self.all_points[0] = self.head_pos

    def move(self):
        self.move_tail()
        self.head_pos.move(self.speed)
        self.all_points.appendleft(Util.Point(self.head_pos.x, self.head_pos.y))

    def turn_up(self):
        self.speed = SpeedConstants.forward_speed

    def turn_down(self):
        self.speed = SpeedConstants.backward_speed

    def turn_left(self):
        self.speed = SpeedConstants.left_speed

    def turn_right(self):
        self.speed = SpeedConstants.right_speed

    def buff(self):
        self.buffed = True

    def size(self):
        return len(self.all_points)