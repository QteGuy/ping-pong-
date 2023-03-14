import pygame as pygame
SPR_SIZE = (10, 100)
WND_SIZE = (1920, 1080)
FPS = 60
window = pygame.display.set_mode(WND_SIZE)
background = pygame.transform.scale(pygame.image.load("pingpong_bg.jpeg"), WND_SIZE)
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, pos_x, pos_y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_name), SPR_SIZE)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 730:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 730:
            self.rect.y += self.speed

