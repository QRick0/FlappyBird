import pygame
import sys
import background, floor, player, pipe, start_game, score, game_over

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load font
font = pygame.font.Font("Fonts/Font.ttf", 32)  

# Create clock
clock = pygame.time.Clock()

# Variables
counter = 0
fps = 60
animation_speed = fps // 5
gravity = 0.5
jump_delay = fps // 4
jump_delay_counter = 0
spawn_counter = 0
spawn_delay = fps

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start Game
    if start_game.start_game == False:
        start_game.start_game = start_game.game_start(start_game.start_game, screen)
    
    # Draw background
    screen.blit(background.bg_image, (background.bg_pos, 0))
    screen.blit(background.bg_image, (background.bg_pos2, 0))

    # Spawn pipe
    pipe.bp_y, spawn_counter, pipe.bp_x, pipe.tp_y, pipe.tp_x = pipe.spawn_pipe(spawn_counter, spawn_delay, pipe.bp_y, pipe.bp_x, pipe.tp_y, pipe.tp_x)

    screen .blit(pipe.bottom_pipe,(pipe.bp_x, pipe.bp_y))
    screen .blit(pipe.top_pipe,(pipe.tp_x, pipe.tp_y))

    # Draw floor
    screen.blit(floor.fl_image, (floor.fl_pos - floor.fl_image.get_width(), background.bg_image.get_height() - floor.fl_image.get_height()))
    screen.blit(floor.fl_image, (floor.fl_pos, background.bg_image.get_height() - floor.fl_image.get_height()))
    screen.blit(floor.fl_image, (floor.fl_pos + floor.fl_image.get_width(), background.bg_image.get_height() - floor.fl_image.get_height()))

    #Move background and floor
    background.bg_pos, background.bg_pos2 = background.move_background(background.bg_pos, background.bg_pos2, background.bg_move, background.bg_image)
    floor.fl_pos = floor.move_floor(floor.fl_pos, floor.fl_move)

    # Update Player animation
    player.player, counter = player.player_animation(counter, player.player, animation_speed) 

    # Draw Player
    screen.blit(player.player, (player.x_pos, player.y_pos))

    # player movement  
    player.vel_y, player.y_pos, player.jumping, jump_delay_counter = player.player_jump(jump_delay, jump_delay_counter, player.vel_y, gravity, player.y_pos, (background.bg_image.get_height() - floor.fl_image.get_height() - 30), player.jump_strength, player.jumping)

    # Move pipe
    pipe.bp_x, pipe.tp_x = pipe.move_pipe(pipe.bp_x, pipe.tp_x)

    # Update score
    score.point_avb, score.score = score.get_score(screen, font, score.score, score.point_avb, score.score_sound)

    # Update Display
    pygame.display.flip()

    # Inc counter
    counter += 1
    jump_delay_counter += 1
    spawn_counter += 1

    # Check if game is over
    if not game_over.end_game:
        game_over.end_game = game_over.game_over(game_over.end_game)

    # Set FPS
    clock.tick(fps)

pygame.quit()
sys.exit()