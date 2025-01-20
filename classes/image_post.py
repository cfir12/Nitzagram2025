import pygame
from constants import *
from helpers import *
from classes.Post import Post


class ImagePost(Post):
    def __init__(self, username, location, description, src):
        super().__init__(username, location, description)
        self.src = src

    def display(self):
        image = pygame.image.load(self.src)
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
        super().display()
