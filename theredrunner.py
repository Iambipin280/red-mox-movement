import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Simple Pygame App")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the initial position and size of the square
x = screen_width // 2
y = screen_height // 2
square_size = 50
speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the key press events
    keys = pygame.key.get_pressed()

    # Move the square based on key presses
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Prevent the square from going outside the screen
    x = max(0, min(x, screen_width - square_size))
    y = max(0, min(y, screen_height - square_size))

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the red square
    pygame.draw.rect(screen, RED, (x, y, square_size, square_size))

    # Update the screen
    pygame.display.update()

    # Set the frames per second
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
