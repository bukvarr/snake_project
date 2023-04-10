import pygame

import Colors
import GameConstants

pygame.font.init()


class Menu:

    default_font = pygame.font.SysFont('arial', 20)
    title_font = pygame.font.SysFont('arial', 50)
    title_text = title_font.render('Snake Game', True, Colors.WHITE)
    start_text = default_font.render('Press 1-5 to select level', True, Colors.WHITE)
    records_text = default_font.render('Press R to view records', True, Colors.WHITE)
    exit_text = default_font.render('Press ESC to exit', True, Colors.WHITE)
    clear_records_text = default_font.render('Press C to clear', True, Colors.WHITE)

    def draw_menu(self, screen):
        screen.fill(Colors.BLACK)
        screen.blit(self.title_text, GameConstants.title_text_pos)
        screen.blit(self.start_text, GameConstants.start_text_pos)
        screen.blit(self.records_text, GameConstants.records_text_pos)
        screen.blit(self.exit_text, GameConstants.exit_text_pos)
        pygame.display.update()

    def cut_records(self, records):
        if len(records) > GameConstants.shown_records_number * 2:
            file = open("records.txt", 'w')
            for i in range(GameConstants.shown_records_number):
                file.write(str(records[i]) + '\n')
            file.close()

    def clear_records(self):
        file = open("records.txt", 'w')
        file.close()

    def show_records(self, screen):
        screen.fill(Colors.BLACK)
        file = open("records.txt", 'r')
        records = []
        screen.blit(self.exit_text, GameConstants.exit_text_pos)
        screen.blit(self.clear_records_text, GameConstants.clear_records_text_pos)
        for line in file:
            records.append(int(line))
        records.sort(reverse=True)
        for i in range(GameConstants.shown_records_number):
            if i >= len(records):
                score = '-'
            else:
                score = str(records[i])
            score = self.default_font.render(str(i + 1) + '. ' + score, True, Colors.WHITE)
            screen.blit(score, (GameConstants.score_pos_x, GameConstants.score_pos_y + (i + 1) * GameConstants.score_between_distance))
        file.close()
        pygame.display.update()
        run = True
        self.cut_records(records)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if event.key == pygame.K_c:
                        self.clear_records()
                        run = False
