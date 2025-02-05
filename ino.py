import pygame

class Ino(pygame.sprite.Sprite): # класс одного пришельца
    def __init__(self,screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/ino.png') # загружаем изображение пришельца
        self.rect = self.image.get_rect() # получаем прямоугольник из изображения
        self.rect.x = self.rect.width # получаем прямоугольник экрана
        self.rect.y = self.rect.height # начальная позиция пришельца вверху экрана
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):# вывод пришельца на экран
        self.screen.blit(self.image,self.rect)

    def update(self):
        # перемещение пришельца
        self.y += 0.05
        self.rect.y = self.y