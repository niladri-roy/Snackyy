from os import scandir
import pygame
import time
import random

pygame.init()

colour_1 = (255,255,255) #white
colour_2 = (255,255,102) #yellow
colour_3 = (0,0,0) #black
colour_4 = (213,200,80)
colour_5 = (0,255,0) #green
colour_6 = (255,0,0) #red


box_len = 900
box_height = 600

add_caption = pygame.display.set_mode((box_len , box_height))
pygame.display.set_caption("SNAKYY")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("arial",30,"bold")
score_font = pygame.font.SysFont("arial",45,"bold")

def final_score(score):
    value = score_font.render("Enjoy the snake game ------ Yor score is :" + str(score), True , colour_2)
    add_caption.blit(value, [0,0])

def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption, colour_3, [x[0],x[1],snake_block])


def display_msg(msg,color)
    mssg = display_style.render(msg, True, color)
    
     