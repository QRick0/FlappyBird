import pygame

pygame.mixer.init()

# Settings
vel_y = 0
jumping = False
jump_strength = -9
y_pos = 200
x_pos = 50
flap_sound = pygame.mixer.Sound("Sounds/sfx_wing.wav")
pygame.mixer.Sound.set_volume(flap_sound, 0.4)

# Load Player sprites
bird1 = pygame.image.load("Graphics/Bird1.png")
bird2 = pygame.image.load("Graphics/Bird2.png")
bird3 = pygame.image.load("Graphics/Bird3.png")
bird4 = pygame.image.load("Graphics/Bird4.png")

player = pygame.transform.scale(bird1, (50, 50))

# Player Movement
def player_jump(jump_delay, counter, y_v, grav, y_p, ground_height, jmp_s, jmp):

    # Jump Delay
    if jump_delay <= counter:
        jmp = False
    else:
        jmp = True
     
    # Get key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jmp:
        y_v = jmp_s
        counter = 0
        jmp = True
        pygame.mixer.Sound.play(flap_sound)

    # Apply gravity and update vertical position
    y_v += grav
    y_p += y_v

    # Ground collision
    if y_p >= ground_height:
        y_p = ground_height
        y_v = 0
        jmp = False

    # Sky collision
    if y_p <= -20:
        y_p = 0
        y_v = 0
        jmp = False

    return y_v, y_p, jmp, counter

# Player animation
def player_animation(x, pl, ani_speed):
    if x == ani_speed:
        pl = pygame.transform.scale(bird2, (50, 50)) 
    elif x == ani_speed * 2:
        pl = pygame.transform.scale(bird3, (50, 50))
    elif x == ani_speed * 3:
        pl = pygame.transform.scale(bird4, (50, 50))
    elif x == ani_speed * 4:
        pl = pygame.transform.scale(bird1, (50, 50))
        x = 0
        
    return pl, x