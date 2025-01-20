import pygame
from classes import Post
from constants import *
from helpers import *
from classes.Post import Post


class TextPost(Post):
    def __init__(self, username, location, description, text):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = (0, 0, 0)
        self.background_color = (129, 197, 255)

    def display_text_background(self):
        pygame.draw.rect(screen, self.background_color, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT,))

    def display_text(self):
        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        text = font.render(self.text, True, self.text_color)
        screen.blit(text, center_text(1, text, 1))

    def display(self):
        super().display()
        self.display_text_background()
        self.display_text()


