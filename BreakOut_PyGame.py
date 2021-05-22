import pygame

# Bricks Size 4x8 -> 32x64
# Player size 4x16 -> 32x128

# Screen set
pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
screen_bg = pygame.image.load("assets/atari_screen.png")
screen_bg_pause = pygame.image.load("assets/Start_screen.png")
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
ball_y = 450
ball = pygame.Rect(ball_x, ball_x, 32, 32)

# Game Variables
game_pause = True
cols = 12
rows = 6
brick_height = 32
brick_width = 64.3
# Score
score = 0
updated_score = False
# Position + RGB Color
brick_list = []
# RGB Colors
brick_color_list = [(200, 73, 70), (197, 109, 59), (180, 123, 46),
                    (163, 162, 43), (70, 172, 65), (62, 72, 197)]

# Pause text
menu_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
pause_text = menu_font.render('Press SPACE', True, (255, 255, 255), (0, 0, 0))
pause_text_rect = pause_text.get_rect()
pause_text_rect.center = (650, 500)

# Highest Scores text
menu_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
highest_score_text = menu_font.render(str(score), True, (255, 255, 255), (96, 35, 127))
# First score
highest_score_text_rect_first = highest_score_text.get_rect()
highest_score_text_rect_first.center = (640, 330)
# Second score
highest_score_text_rect_second = highest_score_text.get_rect()
highest_score_text_rect_second.center = (640, 370)
# Third score
highest_score_text_rect_third = highest_score_text.get_rect()
highest_score_text_rect_third.center = (640, 410)
# Fourth score
highest_score_text_rect_fourth = highest_score_text.get_rect()
highest_score_text_rect_fourth.center = (640, 450)
# Fifth score
highest_score_text_rect_fifth = highest_score_text.get_rect()
highest_score_text_rect_fifth.center = (640, 490)


def list_blocks():
    # Define the brick_list
    for row in range(rows):
        for col in range(cols):
            x = 224 + (brick_width * col * 1.08)
            y = 154 + (brick_height * row * 1.16)
            block_react = pygame.Rect(x, y, brick_width, brick_height)
            block2 = [block_react, brick_color_list[row]]
            brick_list.append(block2)


# set mouse hidden
pygame.mouse.set_visible(False)


# Open file score
def open_file_score():
    file = open("score.txt", "r")
    return file.read().split(";")


# Update score
def update_score():
    current_scores = open_file_score()
    score_1 = current_scores[0]
    score_2 = current_scores[1]
    score_3 = current_scores[2]
    score_4 = current_scores[3]
    score_5 = current_scores[4]

    if score > int(score_1):
        score_1 = score
    elif score > int(score_2):
        score_2 = score
    elif score > int(score_3):
        score_3 = score
    elif score > int(score_3):
        score_4 = score
    elif score > int(score_4):
        score_5 = score

    f = open("score.txt", "w")
    f.write(str(score_1) + ";" + str(score_2) + ";" + str(score_3)
            + ";" + str(score_4) + ";" + str(score_5) + ";")
    f.close()


def load_score():
    new_scores = open_file_score()
    score_1 = new_scores[0]
    score_2 = new_scores[1]
    score_3 = new_scores[2]
    score_4 = new_scores[3]
    score_5 = new_scores[4]

    new_highest_score_text = menu_font.render(str(score_1), True, (255, 255, 255), (181, 20, 0))
    screen.blit(new_highest_score_text, highest_score_text_rect_first)
    new_highest_score_text = menu_font.render(str(score_2), True, (255, 255, 255), (163, 113, 0))
    screen.blit(new_highest_score_text, highest_score_text_rect_second)
    new_highest_score_text = menu_font.render(str(score_3), True, (255, 255, 255), (151, 171, 12))
    screen.blit(new_highest_score_text, highest_score_text_rect_third)
    new_highest_score_text = menu_font.render(str(score_4), True, (255, 255, 255), (41, 167, 0))
    screen.blit(new_highest_score_text, highest_score_text_rect_fourth)
    new_highest_score_text = menu_font.render(str(score_5), True, (255, 255, 255), (0, 76, 166))
    screen.blit(new_highest_score_text, highest_score_text_rect_fifth)


# Start the game Cycle
while game_cycle:
    if not brick_list:
        list_blocks()
    # End Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score = 0
                game_pause = False

    if not game_pause:
        # Allow new score
        updated_score = False

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
        # Lose Condition
        if ball_y > 720:
            game_pause = True
            ball_x = 640
            ball_y = 450
            ball = pygame.Rect(ball_x, ball_y, 16, 16)
            pygame.draw.rect(screen, (255, 255, 255), ball)
            screen.blit(pause_text, pause_text_rect)
            pygame.display.update()

        ball = pygame.Rect(ball_x, ball_y, 16, 16)

        # Collider with Player
        if ball.colliderect(player):
            ball_dy *= -1

        # Screen update
        screen.fill((0, 0, 0))
        screen.blit(screen_bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, (255, 255, 255), ball)
        if game_pause:
            screen.blit(pause_text, pause_text_rect)

        # Bricks
        for block in brick_list:
            # Draw Bricks
            pygame.draw.rect(screen, block[1], block[0])

        for block in brick_list:
            if ball.colliderect(block[0]):
                ball_dy *= -1
                brick_list.remove(block)

                # Sum point score
                if block[0][1] == 339:
                    score += 2
                elif block[0][1] == 302:
                    score += 4
                elif block[0][1] == 265:
                    score += 6
                elif block[0][1] == 228:
                    score += 8
                elif block[0][1] == 191:
                    score += 10
                elif block[0][1] == 154:
                    score += 12

    else:
        # Update score
        if not updated_score and score > 0:
            update_score()
            updated_score = True
        # Pause and show score
        screen.blit(screen_bg_pause, (0, 0))
        load_score()

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
