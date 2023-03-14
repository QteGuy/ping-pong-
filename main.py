from data import *

player1 = Player1("player1.png", 10, 10, 5)
player2 = Player2("player2.png", 1420, 10, 5)

game = True
game_over = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if not game_over:
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        player1.update_l()
        player2.update_r()

    clock.tick(FPS)
    pygame.display.update()

