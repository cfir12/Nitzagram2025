import pygame
from classes import Post
from constants import *


class ImagePost(Post):
    def __init__(self, username, location, description):
        super().__init__(self, username, location, description)
        self.image = pygame.image.load("Images/ronaldo.jpg")
        pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))