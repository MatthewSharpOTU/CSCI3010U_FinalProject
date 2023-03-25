import pygame
pygame.init()

WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680

# Set the colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Plinko Board')

# Main game loop
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board background
    window.fill(WHITE)

    # Draw the slots
    #for i in range(7):
        #for j in range(10):
           # x = 40 + i * 80 + j % 2 * 40
            #y = 60 + j * 40
           # pygame.draw.circle(window, BLUE, (x, y), 18)

    pygame.draw.circle(window, GRAY, (660, 80), 5)
    pygame.draw.circle(window, GRAY, (660, 160), 5)
    pygame.draw.circle(window, GRAY, (660, 240), 5)
    pygame.draw.circle(window, GRAY, (660, 320), 5)
    pygame.draw.circle(window, GRAY, (660, 400), 5)
    pygame.draw.circle(window, GRAY, (660, 480), 5)
    pygame.draw.circle(window, GRAY, (660, 560), 5)

    # Draw the pegs
    for i in range(7):
        for j in range(13):
            x = 100 + i * 80 + j % 2 * 40
            y = 80 + j * 40
            pygame.draw.circle(window, GRAY, (x, y), 5)

    pygame.draw.line(window, BLACK, (100, 80), (100, 600))
    pygame.draw.line(window, BLACK, (660, 80), (660, 600))
    pygame.draw.line(window, BLACK, (100, 600), (660, 600))

    pygame.draw.line(window, BLACK, (180, 560), (180, 600))
    pygame.draw.line(window, BLACK, (260, 560), (260, 600))
    pygame.draw.line(window, BLACK, (340, 560), (340, 600))
    pygame.draw.line(window, BLACK, (420, 560), (420, 600))
    pygame.draw.line(window, BLACK, (500, 560), (500, 600))
    pygame.draw.line(window, BLACK, (580, 560), (580, 600))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
