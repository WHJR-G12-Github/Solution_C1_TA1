# Importing 'pygame' 
import pygame

# Initialising 'pygame' 
pygame.init()

# Creating game window of width 400 and height 600
screen = pygame.display.set_mode((400,600))

# Setting the title of the game
pygame.display.set_caption("Shooting Spaceship")

# Loading the background image
background_image = pygame.image.load("bg2.jpg").convert()

# Displaying the 'background_image' at the location [0,0]
screen.blit(background_image,[0,0])

# Updating the screen after adding the background image and drawing the rectangle
pygame.display.update()
