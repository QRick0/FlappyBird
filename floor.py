import pygame
import background

# Load Floor Image
fl_image = pygame.image.load("Graphics/Floor.png")

# Set initial floor pos
fl_pos = 0

# Floor Movement Speed
fl_move = 5

# Floor Movement
def move_floor(x, move):

    # Move Floor
    x -= move

    # Reset bg_image after it leave screen
    if x <= 0 - background.bg_image.get_width():
        x = background.bg_image.get_width()
    
    return x