import pygame
from classes import Post
from constants import *
from helpers import *


class ImagePost(Post):
    def __init__(self, username, location, description, image):
        super().__init__(self, username, location, description)
        self.image = image

    def display(self):
        self.image = pygame.image.load("Images/ronaldo.jpg")
        pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
