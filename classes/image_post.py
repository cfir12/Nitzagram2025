import pygame
from classes import Post
from constants import *
from helpers import *


class ImagePost(Post):
    def __init__(self, username, location, description, src):
        super().__init__(self, username, location, description)
        self.src = src

    def display(self):
        image = pygame.image.load(self.src)
        pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
        super().display()
