import pygame
import background, floor, player

pygame.mixer.init()

# Varibles
s_screen = pygame.image.load("Graphics/Start_Screen.png")
start_game = False
clock = pygame.time.Clock()
flap_sound = pygame.mixer.Sound("Sounds/sfx_wing.wav")
pygame.mixer.Sound.set_volume(flap_sound, 0.4)


# Start game function
def game_start(s, screen):
    counter = 0
    animation_speed = 60 // 5

    while not s:

        # Draw background
        screen.blit(background.bg_image, (background.bg_pos, 0))
        screen.blit(background.bg_image, (background.bg_pos2, 0))

        # Draw Floor
        screen.blit(floor.fl_image, (floor.fl_pos - floor.fl_image.get_width(), background.bg_image.get_height() - floor.fl_image.get_height()))
        screen.blit(floor.fl_image, (floor.fl_pos, background.bg_image.get_height() - floor.fl_image.get_height()))
        screen.blit(floor.fl_image, (floor.fl_pos + floor.fl_image.get_width(), background.bg_image.get_height() - floor.fl_image.get_height()))

        # Update Player animation
        player.player, counter = player.player_animation(counter, player.player, animation_speed) 

        # Draw Player
        screen.blit(player.player, (50,player.y_pos))

        # Draw start Screen
        screen.blit(s_screen, (100,50))

        #Move background and floor
        background.bg_pos, background.bg_pos2 = background.move_background(background.bg_pos, background.bg_pos2, background.bg_move, background.bg_image)
        floor.fl_pos = floor.move_floor(floor.fl_pos, floor.fl_move)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not s:
            player.vel_y = player.jump_strength
            pygame.mixer.Sound.play(flap_sound)
            s = True

        # Update Display
        pygame.display.flip()

        # Inc counter
        counter += 1

        clock.tick(60)
    return s