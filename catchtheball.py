import pygame
import random
import sys
import webbrowser
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

basket = pygame.Surface((80, 20))
basket.fill((0, 150, 255))
ball = pygame.Surface((20, 20))
pygame.draw.circle(ball, (255, 100, 0), (10, 10), 10)


basket_x = WIDTH // 2
basket_y = HEIGHT - 40
basket_speed = 7

ball_x = random.randint(20, WIDTH - 20)
ball_y = 0
ball_speed = 4

score = 0
lives = 3
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()


running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - 80:
        basket_x += basket_speed

   
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(20, WIDTH - 20)
        lives -= 1

   
    if (basket_y - 20 < ball_y < basket_y) and (basket_x < ball_x < basket_x + 80):
        score += 1
        ball_y = 0
        ball_x = random.randint(20, WIDTH - 20)
        ball_speed += 0.2 

  
    screen.blit(basket, (basket_x, basket_y))
    screen.blit(ball, (ball_x, ball_y))

    
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 100, 10))

    
    if lives <= 0:
        if score==10:
            score=0
            lives=3
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        game_over_text = font.render("GAME OVER! Press R to Restart or Q to Quit", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(200)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            score = 0
            lives = 3
            ball_speed = 4
        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        continue

    pygame.display.flip()
    clock.tick(60)
