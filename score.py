import pygame
import pipe, player

pygame.mixer.init()
    
score = 0
point_avb = True
score_sound = pygame.mixer.Sound("Sounds/point.wav")
pygame.mixer.Sound.set_volume(score_sound, 0.3)
 

# Update and draw score
def get_score(screen, fo, sc, pa, ss):

    if player.x_pos > pipe.bp_x and player.x_pos < pipe.bp_x + pipe.bottom_pipe.get_width() and pa == True:
        pa = False
        sc += 1
        pygame.mixer.Sound.play(ss)

    text = fo.render(f"Score: {sc}", True, (0,0,0))
    text_box = text.get_rect()


    screen.blit(text, text_box)
    return pa, sc