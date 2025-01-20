import helpers
from helpers import screen
import pygame
from constants import *


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        comment = font.render(self.text, True, BLACK)
        screen.blit(comment, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + comment_num * COMMENT_LINE_HEIGHT))
