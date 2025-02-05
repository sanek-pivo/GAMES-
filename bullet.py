import pygame

class Bullet(pygame.sprite.Sprite): # создаем пулю
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 139,195,74
        self.speed = 4
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self): # перемещение пули
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self): # рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)
