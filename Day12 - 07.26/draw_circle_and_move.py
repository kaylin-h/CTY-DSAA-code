import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
snake_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
moving_speed = 100
screen_color = "lightgreen"
snake_x = 30
snake_y = 30
snake_length = 20
snake_width = 20
circle_radius = 10
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(screen_color)
    #f"{screen_color}"
    pygame.draw.circle(screen, "dark blue", circle_pos, circle_radius)
    snake_box = pygame.Rect(snake_x, snake_y, snake_length, snake_width)
    pygame.draw.rect(screen, "dark green", snake_box)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_pos.y -= moving_speed * dt
    if keys[pygame.K_DOWN]:
        circle_pos.y += moving_speed * dt
    if keys[pygame.K_LEFT]:
        circle_pos.x -= moving_speed * dt
    if keys[pygame.K_RIGHT]:
        circle_pos.x += moving_speed * dt

    if keys[pygame.K_w]:
        snake_y -= moving_speed * dt
    if keys[pygame.K_s]:
        snake_y += moving_speed * dt
    if keys[pygame.K_a]:
        snake_x -= moving_speed * dt
    if keys[pygame.K_d]:
        snake_x += moving_speed * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
    #print(f"x2-x1: {float(snake_x - circle_pos.x)}, y2-y1: {float(snake_x - circle_pos.x)}")
    if abs(float(snake_x - circle_pos.x)) < 10 and abs(float(snake_y - circle_pos.y)) < 10:
        print("collision")
        circle_radius += 10 * dt
        snake_length += moving_speed * dt
        

    '''
    old_color = screen_color
    try:
        old_color = screen_color
        new_color = input("Change color: ")
        screen.fill(f"{new_color}")
        screen_color = new_color

    except:
        screen_color = old_color

    '''
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()