import Util

WIDTH = 500
HEIGHT = 500
start_upd_rate = 17
max_upd_rate = 60

snake_start_pos = Util.Point(WIDTH // 2, HEIGHT // 2)
coin_start_pos = Util.Point(WIDTH // 2, (HEIGHT // 5))

object_size = 10

title_text_pos = (117, 70)
start_text_pos = (143, 400)
records_text_pos = (277, 10)
exit_text_pos = (10, 10)
score_text_pos = (332, 13)
final_score_text_pos = (163, 100)
clear_records_text_pos = (10, 465)
pause_text_pos = (12, 13)

score_text_size = (158, 30)
pause_text_size = (270, 20)

shown_records_number = 5
score_pos_x = 30
score_pos_y = 20
score_between_distance = 25

super_coin_spawn_rate = 6
super_coin_score_buff = 15