import pygame
from sys import exit
running = True
funny_joke_in_code_haha = 'fart'
ver = 'Pre-Release 1.0.0'

def log(string):
    print(string)
def background(r,g,b):
    background_colour = (r, g, b)
def set_display_mode(width, height):
    screen = pygame.display.set_mode((width, height))
def caption(name):
    pygame.display.set_caption(name)
def build_window():
    screen.fill(background_colour)
    pygame.display.flip()
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False  # Be IDLE friendly
pygame.quit()
