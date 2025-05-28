import pygame

# Load background Image
bg_image = pygame.image.load("Graphics/Background.png")

# Set initial background pos
bg_pos = 0
bg_pos2 = bg_image.get_width()

# Background Movement Speed
bg_move = 1

# Background Movement
def move_background(x, x2, move, img):

    # Move Background
    x -= move
    x2 -= move

    # Reset bg_image after it leave screen
    if x == -1 * img.get_width():
        x = img.get_width()

    if x2 == -1 * img.get_width():
        x2 = img.get_width()
    
    return x, x2