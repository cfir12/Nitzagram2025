import pygame

from classes.TextPost import TextPost
from classes.image_post import ImagePost
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    username = "noa"
    post_ronaldo = ImagePost(username, "portugal", "gdxfcgh",'Images/ronaldo.jpg')
    post_noakirel = ImagePost(username, "israel", "singing",'Images/noa_kirel.jpg')
    ttext = TextPost(username, "xxx", "swws", "hello")
    list_posts = [post_noakirel, post_ronaldo, ttext]
    current_post = 0

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_button(like_button, pos):
                    list_posts[current_post].add_like()
                if mouse_in_button(click_post_button, pos):
                    if current_post < 2:
                        current_post += 1
                    else:
                        current_post = 0
                if mouse_in_button(comment_button, pos):
                    comment = read_comment_from_user()
                    list_posts[current_post].add_comment(comment)

            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        list_posts[current_post].display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
