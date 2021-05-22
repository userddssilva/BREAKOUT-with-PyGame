import random
import pygame
# Bricks Size 4x8 -> 32x64
# Player size 4x16 -> 32x128

# Screen set
pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
screen_bg = pygame.image.load("assets/atari_screen.png")
game_clock = pygame.time.Clock()
game_cycle = True

# SoundTrack
pygame.mixer.music.load("assets/soundtrack.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

# Player
player_move_left = False
player_move_right = False
player_x = 640
player_score = 0

# Ball
ball_dx = 5
ball_dy = 10
ball_x = 640
ball_y = 360
ball = pygame.Rect(ball_x, ball_x, 32, 32)

# Game Variables
cols = 12
rows = 6
brick_height = 32
brick_width = 64.3
# Position + RGB Color
brick_list = []
# RGB Colors
brick_color_list = [(200, 73, 70), (197, 109, 59), (180, 123, 46),
                    (163, 162, 43), (70, 172, 65), (62, 72, 197)]
# Define the brick_list
for row in range(rows):
    for col in range(cols):
        x = 224 + (brick_width * col * 1.08)
        y = 154 + (brick_height * row * 1.16)
        block = pygame.Rect(x, y, brick_width, brick_height)
        block2 = [block, brick_color_list[row]]
        brick_list.append(block2)


# set mouse hidden
pygame.mouse.set_visible(False)

# Start the game Cycle
while game_cycle:

    # End Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False

    # Player Movement
    player_XY = pygame.mouse.get_pos()

    player_x = player_XY[0] // 1
    if player_x > 928:
        player_x = 928
    if player_x < 224:
        player_x = 224
    player = pygame.Rect(player_x, 664, 128, 16)

    # Ball Movement
    ball_x += ball_dx
    ball_y += ball_dy
    # Colliders
    if ball_x < 224:
        ball_dx *= -1
    if ball_x > 1040:
        ball_dx *= -1
    if ball_y < 104:
        ball_dy *= -1
    if ball_y > 720:
        # YOU LOSE
        ball_dy *= -1
    ball = pygame.Rect(ball_x, ball_y, 16, 16)

    # Collider with Player
    if ball_y > 658 and not (ball_y > 700):
        if player_x < ball_x + 150:
            if player_x + 150 > ball_x:
                ball_y = 658
                ball_dy *= -1

    # Screen update
    screen.fill((0, 0, 0))
    screen.blit(screen_bg, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), ball)

    color_try = 0
    color_row = 0

    # Bricks
    for block in brick_list:
        # Select Color
        if color_row > 5:
            color_row = 0
        # Draw Bricks
        pygame.draw.rect(screen, block[1], block[0])

        # Count color at List
        color_try += 1
        if (color_try // 13) == 1:
            color_row += 1
            color_try = 0

    for block in brick_list:
        if ball.colliderect(block[0]):
            ball_dy *= -1
            brick_list.remove(block)

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
