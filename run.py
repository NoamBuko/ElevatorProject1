import pygame
from settings import *
from building import Building

building = Building()

pygame.init()

# draw screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
background = pygame.image.load(BACKGROUND_PIC)
background = pygame.transform.scale(background, ((SCREEN_WIDTH, SCREEN_HEIGHT)))

# run while loop
run = True
while run:
    clock.tick(60)
    screen.fill('white')
    #screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                building.scroll_down_all()
            elif event.button == 5:  # Scroll down
                building.scroll_up_all()
            else:
                position = event.pos
    
                building.check_for_new_calls(position)


    building.update_all()
    building.draw_all(screen)
    
    pygame.display.update()

pygame.quit()
