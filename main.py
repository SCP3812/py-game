import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basic Pygame Example")

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

# Rectangle settings
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50
rect_speed = 5
rect1_x = 0
rect1_y = 300
rect1_width = 1000
rect1_height = 1000


class Player():
    def __init__(self, rectx, recty, rectw, recth, rects):
        self.rectx = rectx
        self.recty = recty
        self.rectw = rectw
        self.recth = recth
        self.rects = rects
        self.rect = self.image.get_rect()

    def gravity(self):
        self.recty += 3.2
    


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move rectangle
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed

    player1 = Player(rect_x, rect_y, rect_width, rect_height, rect_speed)
    rect = pygame.Rect(player1)
    rect1 = pygame.Rect(rect1_x, rect1_y, rect1_height, rect1_width)
    list_of_rects = [rect1]

    result = rect.collideobjects(list_of_rects)
    if result != None:
        print(result)
        rect_y -= rect_speed
    else: 
        pass

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the red rectangle
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, BLUE, rect1)

    # Update the display
    pygame.display.flip()

    # Set frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
