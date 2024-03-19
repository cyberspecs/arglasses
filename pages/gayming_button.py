import pygame
import os
import sys
# from main import WIDTH, HEIGHT
# import screen from main
pygame.init()
draw_params = []
# print (WIDTH)
display_info = pygame.display.Info()
WIDTH = display_info.current_w - 100
HEIGHT = display_info.current_h - 100


Red = (255, 0, 0)

clicks = 0

def is_even(number):
    return number % 2 == 0


basketrandom = pygame.transform.scale(pygame.image.load(os.path.join('png', 'basketrandom_logo.jpg')), (200,200))
flappybird = pygame.transform.scale(pygame.image.load(os.path.join('png', 'flappybird_logo.png')), (200,200))


def show(game, event, buttonsnum):
    global clicks, draw_params
    clicks += 1
    box = pygame.Rect(0, 0, 200, 32)
    text = str(clicks)
    font = pygame.font.Font(None, 32)
    text = font.render(text, True, (255, 255, 255))
    # draw_params.append((pygame.draw.rect, (game.get('screen'), (0, 0, 0), box)))
    # draw_params.append((game.get('screen').blit, (text, (10, 10))))
    try:
        if len(draw_params) > 0:
            draw_params = []
            pass
        else:
            draw_params.append((game.get("screen").blit, (basketrandom, (450, 250))))
            draw_params.append((game.get("screen").blit, (flappybird, (800, 250))))


    except Exception as e:
        print("Error:", e)
        pass

def hide():
    global draw_params
    draw_params = []
    pass

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])