import sys

import pygame

def check_keydown_events(event, ship):
    #Реагирует на нажатие клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # ВАНЯ: дописал тебе  -> 
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True        
    # ВАНЯ: дописал тебе  <-

def check_keyup_events(event, ship):
    #Реагирует на отпускание клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # ВАНЯ: дописал тебе  -> 
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False        
    # ВАНЯ: дописал тебе  <-

def check_events(ship):
    #Обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)     
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    #Перерисовывает экран при каждом проходе основного цикла
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
            
