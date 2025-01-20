import pygame
from helpers import *
from constants import *
from helpers import screen


class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.counter_likes = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.counter_likes += 1

    def add_comment(self, text):
        self.comments.append(text)

    def display_location(self):
        screen.blit(self.location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

    def display_likes(self):
        screen.blit(self.counter_likes, (LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS))

    def display_username(self):
        screen.blit(self.username, (USER_NAME_X_POS, USER_NAME_Y_POS))
        להוסיף פונטים#

    def display_description(self):
        screen.blit(self.description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def display(self):
        self.display_likes()
        self.display_comments()
        self.display_username()
        self.display_location()
        self.display_description()


