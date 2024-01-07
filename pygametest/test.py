import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dotted Line")

# Set up colors
white = (255, 255, 255)

# Set up dotted line parameters
line_width = 15
dot_spacing = 30


def drawLine():
    for y in range(0, height, dot_spacing * 2):
        pygame.draw.rect(screen, "white", ((width // 2, y), (line_width, line_width)))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the dotted line

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
