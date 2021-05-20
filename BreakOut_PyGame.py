import pygame

# Screen set
pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
screen_bg = pygame.image.load("assets/atari_screen.png")
game_clock = pygame.time.Clock()
game_cycle = True

# Player
player = pygame.image.load("assets/player.png")
player_move_left = False
player_move_right = False

# Ball
ball = pygame.image.load("assets/ball.png")
ball_dx = 5
ball_dy = 7
ball_x = 640
ball_y = 360

pygame.mouse.set_visible(False)

while game_cycle:
    # End Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False

    # Player Movement
    player_XY = pygame.mouse.get_pos()
    player_x = player_XY[0]
    if player_x > 850:
        player_x = 850

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

    # Collider with Player
    if ball_y > 680 and not (ball_y > 700):
        if player_x < ball_x + 150:
            if player_x + 150 > ball_x:
                ball_y = 680
                ball_dy *= -1

    # Screen update
    screen.fill((0, 0, 0))
    screen.blit(screen_bg, (0, 0))
    screen.blit(player, (player_x, 680))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
