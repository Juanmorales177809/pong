import pygame
from pong_POO_2 import Pong
from ball import Ball


class Player:
    def __init__(self):
        self.rect_x = 400 #Starting coordinates of the paddle
        self.rect_y = 580
        self.rect_change_x = 0 #initial speed of the paddle
        self.rect_change_y = 0
        self.width = 100
        self.tall = 20
        
    
    def drawrect(self,juego):#draws the paddle. Also restricts its movement between the edges of the window.
        if self.rect_x <= 0:
            self.rect_x = 0
        if self.rect_x >= 699:
            self.rect_x = 699
        pygame.draw.rect(juego.screen,juego.red,[self.rect_x,self.rect_y,self.width,self.tall])

