import random

import Colors
import GameObjects
import Map
import pygame
import GameConstants
import Menu
import SpeedConstants
import sys


class Game:

    run = True
    game_run = True
    my_map = Map.Map()
    upd_rate = GameConstants.start_upd_rate
    menu = Menu.Menu()
    lvl = 1
    score = 0

    def render_walls(self, screen):
        for wall in self.my_map.walls:
            surf = pygame.Surface((GameConstants.object_size, GameConstants.object_size))
            surf.fill(wall.color)
            screen.blit(surf, (wall.head_pos.x, wall.head_pos.y))

    def render_coin(self, screen):
        surf = pygame.Surface((GameConstants.object_size, GameConstants.object_size))
        surf.fill(self.my_map.coin.color)
        screen.blit(surf, (self.my_map.coin.head_pos.x, self.my_map.coin.head_pos.y))

    def render_snake(self, screen):
        for part in self.my_map.snake.all_points:
            surf = pygame.Surface((GameConstants.object_size, GameConstants.object_size))
            surf.fill(self.my_map.snake.color)
            screen.blit(surf, (part.x, part.y))
        if not self.my_map.snake.buffed:
            surf = pygame.Surface((GameConstants.object_size, GameConstants.object_size))
            surf.fill(Colors.BLACK)
            screen.blit(surf, (self.my_map.snake.deleted_part.x, self.my_map.snake.deleted_part.y))

    def coin_eaten(self):
        return self.my_map.snake.intersects_with(self.my_map.coin)

    def crashed(self):
        for wall in self.my_map.walls:
            if self.my_map.snake.intersects_with(wall):
                return True
        if self.my_map.snake.intersects_itself():
            return True
        return False

    def pause_game(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False

    def processing_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.my_map.snake.speed != SpeedConstants.right_speed:
                        self.my_map.snake.turn_left()
                elif event.key == pygame.K_RIGHT:
                    if self.my_map.snake.speed != SpeedConstants.left_speed:
                        self.my_map.snake.turn_right()
                elif event.key == pygame.K_UP:
                    if self.my_map.snake.speed != SpeedConstants.backward_speed:
                        self.my_map.snake.turn_up()
                elif event.key == pygame.K_DOWN:
                    if self.my_map.snake.speed != SpeedConstants.forward_speed:
                        self.my_map.snake.turn_down()
                elif event.key == pygame.K_SPACE:
                    self.pause_game()
                elif event.key == pygame.K_ESCAPE:
                    self.game_run = False

    def draw_menu(self, screen):
        run_menu = True
        self.menu.draw_menu(screen)
        while run_menu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        run_menu = False
                        self.game_run = True
                        self.lvl = 1
                    elif event.key == pygame.K_2:
                        run_menu = False
                        self.game_run = True
                        self.lvl = 2
                    elif event.key == pygame.K_3:
                        run_menu = False
                        self.game_run = True
                        self.lvl = 3
                    elif event.key == pygame.K_4:
                        run_menu = False
                        self.game_run = True
                        self.lvl = 4
                    elif event.key == pygame.K_5:
                        run_menu = False
                        self.game_run = True
                        self.lvl = 5
                        self.my_map.snake.speed = SpeedConstants.left_speed
                    elif event.key == pygame.K_r:
                        self.menu.show_records(screen)
                        self.menu.draw_menu(screen)
                    elif event.key == pygame.K_ESCAPE:
                        run_menu = False
                        self.game_run = False
                        self.run = False
            pygame.time.wait(10)

    def render_score(self, screen):
        surf = pygame.Surface(GameConstants.score_text_size)
        surf.fill(Colors.BLACK)
        screen.blit(surf, GameConstants.score_text_pos)
        score_font = pygame.font.SysFont('arial', 30)
        score_text = score_font.render('Score: ' + str(self.score), True, Colors.WHITE)
        screen.blit(score_text, GameConstants.score_text_pos)

    def render_pause_text(self, screen):
        surf = pygame.Surface(GameConstants.pause_text_size)
        surf.fill(Colors.BLACK)
        screen.blit(surf, GameConstants.pause_text_pos)
        score_font = pygame.font.SysFont('arial', 17)
        score_text = score_font.render('Press SPACE to pause or continue', True, Colors.WHITE)
        screen.blit(score_text, GameConstants.pause_text_pos)

    def end_game(self, screen):
        file = open("records.txt", 'a')
        file.write(str(self.score) + '\n')
        file.close()
        screen.fill(Colors.BLACK)
        score_font = pygame.font.SysFont('arial', 30)
        score_text = score_font.render('Final Score: ' + str(self.score), True, Colors.WHITE)
        screen.blit(score_text, GameConstants.final_score_text_pos)
        pygame.display.update()
        run_end = True
        while run_end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_end = False
            pygame.time.wait(10)
        file.close()

    def update_score(self):
        if self.my_map.super_coin_spawned:
            self.score += GameConstants.super_coin_score_buff
        else:
            self.score += 1

    def draw_game(self, screen, clock):
        self.my_map.restart()
        screen.fill(Colors.BLACK)
        self.my_map.set_border_walls()
        self.my_map.set_additional_walls(self.lvl)
        Game.render_walls(self, screen)
        Game.render_coin(self, screen)
        while self.game_run:
            clock.tick(self.upd_rate)
            Game.my_map.snake.move()
            Game.render_score(self, screen)
            Game.render_pause_text(self, screen)
            Game.render_snake(self, screen)
            self.render_coin(screen)
            pygame.display.update()
            if self.coin_eaten():
                self.my_map.snake.buff()
                self.update_score()
                self.my_map.set_new_coin()
            if self.crashed():
                self.game_run = False
            self.processing_event()
            self.upd_rate = min(GameConstants.start_upd_rate + self.my_map.snake.size() \
                                // SpeedConstants.speed_update_period, GameConstants.max_upd_rate)

    def start_game(self):
        pygame.init()
        screen = pygame.display.set_mode((GameConstants.WIDTH, GameConstants.HEIGHT))
        pygame.display.set_caption("Snake")
        clock = pygame.time.Clock()
        while self.run:
            self.draw_menu(screen)
            self.draw_game(screen, clock)
            if self.run:
                Game.end_game(self, screen)


