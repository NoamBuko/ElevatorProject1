import pygame
from settings import *

class Gap:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.gap_img = pygame.image.load(GAP_PIC)
        self.gap_img = pygame.transform.scale(self.gap_img, (GAP_WIDTH, GAP_HEIGHT))

    
    def draw(self, screen):
        screen.blit(self.gap_img, (self.x, self.y))


    def scroll_up(self):
        self.y -= SCROLL_SPEED

    def scroll_down(self):
        self.y += SCROLL_SPEED
