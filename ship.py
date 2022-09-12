import pygame

class Ship():

    def __init__(self, ai_settings, screen):
    #Инициализирует корабль и задает его начальную позицию

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('ship7.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #Сохранение вещественной координаты центра корабля
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.velocityx = float(0)
        self.velocityy = float(0)
        

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        # ВАНЯ: дописал тебе  -> 
        self.moving_up = False
        self.moving_down = False
        # ВАНЯ: дописал тебе  <-   

    def update(self):
        #Обновляет позицию корабля с учетом флагов

        #Обновляется атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.velocityx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.velocityx -= self.ai_settings.ship_speed_factor
       
        if self.moving_up: #and self.rect.top > 0:
            self.velocityy -= self.ai_settings.ship_speed_factor

        if self.moving_down: #and self.rect.bottom > 0:
            self.velocityy += self.ai_settings.ship_speed_factor
            

        self.centerx += self.velocityx
        self.centery += self.velocityy

        #Обновление атрибута rect на основании self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        #Вывод изображения корабля на экран
        self.screen.blit(self.image, self.rect)
        
