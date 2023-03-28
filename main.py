from data import *

player1 = Player1("player1.png", 10, 10, 5, SPR_SIZE)
player2 = Player2("player2.png", 1420, 10, 5, SPR_SIZE)
ball = GameSprite("ball.png", 560, 560, 5, BL_SIZE)
speed_x = 5
speed_y = 5

win1_label = font_label.render("Player 1 wins!", 1, GREEN)
win2_label = font_label.render("Player 2 wins!", 1, GREEN)

game = True
game_over = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if not game_over:
        window.blit(background, (0, 0))
        ball.reset()
        player1.reset()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= WND_SIZE[1] - BL_SIZE[1] or ball.rect.y <= 0:
            speed_y *= -1.1
        if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
            speed_x *= -1.1
        if ball.rect.x <= -50:
            window.blit(win2_label, (640, 360))
        if ball.rect.x >= 1470:
            window.blit(win1_label, (640, 360))
        player1.update_l()
        player2.update_r()

    clock.tick(FPS)
    pygame.display.update()
