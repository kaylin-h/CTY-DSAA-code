import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #pygame.draw.lines(screen, (0, 0, 0), (1, 1), (1, 720))
    #pygame.draw.line(screen, "white", (10, 0), (10, 720))
    
    blockSize = 20 #Set the size of the grid block
    for x in range(0, 10, blockSize):
        for y in range(0, 20, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, "white", rect, 1)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()