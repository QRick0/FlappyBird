import pygame
import random
import background, floor, score

# Load Images
bottom_pipe = pygame.transform.scale(pygame.image.load("Graphics/Pipe.png"), (75, 400))
top_pipe = pygame.transform.rotate(bottom_pipe, 180)

# Constants
pipe_gap = 125

# Positions
bp_x = background.bg_image.get_width()
bp_y = 0 + (random.randint(pipe_gap, background.bg_image.get_height() - floor.fl_image.get_height()))

tp_x = background.bg_image.get_width()
tp_y = bp_y - top_pipe.get_height() - pipe_gap

# Move pipe
def move_pipe(x, x2):
    x -= floor.fl_move
    x2 -= floor.fl_move
    return x, x2

# Spawn pipe
def spawn_pipe(sc, sd, y, x, y2, x2):
    if sc >= sd and x < 0 - bottom_pipe.get_width():
        y = 0 + (random.randint(pipe_gap, background.bg_image.get_height() - floor.fl_image.get_height()))
        x = background.bg_image.get_width()
        y2 = y - top_pipe.get_height() - pipe_gap
        x2 = x
        sc = 0
        score.point_avb = True
    
    return y, sc, x, y2, x2