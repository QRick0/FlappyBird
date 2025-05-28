import pygame
import time
import random
import player, pipe, floor, background, score, start_game

# Varibles
end_game = False
clock = pygame.time.Clock()
pygame.mixer.init()
death_sound = pygame.mixer.Sound("Sounds/hit.wav")
pygame.mixer.Sound.set_volume(death_sound, 0.3)

# Reset game
def reset_game():
    score.score = 0
    score.point_avb = True
    player.vel_y = 0
    player.jumping = False
    player.jump_strength = -9
    player.y_pos = 200
    player.x_pos = 50
    pipe.bp_x = background.bg_image.get_width()
    pipe.bp_y = 0 + (random.randint(pipe.pipe_gap, background.bg_image.get_height() - floor.fl_image.get_height()))
    pipe.tp_x = background.bg_image.get_width()
    pipe.tp_y = pipe.bp_y - pipe.top_pipe.get_height() - pipe.pipe_gap
    floor.fl_pos = 0
    background.bg_pos = 0
    background.bg_pos2 = background.bg_image.get_width()
    start_game.start_game = False
    player.player = pygame.transform.scale(player.bird1, (50, 50))

# End game function
def game_over(o):

    #Check for crashes
    # Floor
    if player.y_pos >= background.bg_image.get_height() - floor.fl_image.get_height() - 30:
        pygame.mixer.Sound.play(death_sound)
        o = True

    # Ceiling
    if player.y_pos <= -15:
        pygame.mixer.Sound.play(death_sound)
        o = True

    # Bottom pipe
    if player.x_pos > pipe.bp_x and player.x_pos < pipe.bp_x + pipe.bottom_pipe.get_width() and player.y_pos + 10 > pipe.bp_y:
        pygame.mixer.Sound.play(death_sound)
        o = True

    if player.x_pos + 50 > pipe.bp_x and player.x_pos + 50 < pipe.bp_x + pipe.bottom_pipe.get_width() and player.y_pos + 40 > pipe.bp_y:
        pygame.mixer.Sound.play(death_sound)
        o = True

    # Top pipe
    if player.x_pos > pipe.tp_x and player.x_pos < pipe.tp_x + pipe.top_pipe.get_width() and player.y_pos + 10 < pipe.tp_y + pipe.top_pipe.get_height():
        pygame.mixer.Sound.play(death_sound)
        o = True

    if player.x_pos + 50 > pipe.tp_x and player.x_pos + 50 < pipe.tp_x + pipe.top_pipe.get_width() and player.y_pos + 40 < pipe.tp_y + pipe.top_pipe.get_height():
        pygame.mixer.Sound.play(death_sound)
        o = True

    if o:
        time.sleep(0.5)

    while o:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and o:
            player.vel_y = 0
            o = False
            reset_game()
            time.sleep(0.1)

        # Update Display
        pygame.display.flip()

        clock.tick(60)
    return o