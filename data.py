import pygame
SPR_SIZE = (10,100)
WND_SIZE = (1080, 720)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_name), SPR_SIZE)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reset(self):
        pygame.window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

