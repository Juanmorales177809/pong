import pygame
import time


class Pong:
    
    def __init__(self):
        self.size = (800,600)
        self.score = 0
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("pong")#Initializing the display window
        self.clock=pygame.time.Clock()
    
        
    def print_score(self,score,center,size):
        font= pygame.font.SysFont('Calibri', size)
        text = font.render("Score = " + str(score), False, self.white)
        self.screen.blit(text,center)
        #pygame.display.flip()
        
        #score board
    def print_lifes(self, lifes):
        
        font= pygame.font.SysFont('Calibri', 15)
        text = font.render("Lifes = " + str(lifes), False, self.white)
        self.screen.blit(text,[40,10])
        
        #pygame.display.flip()
        
    def print_star(self,num):
        img = pygame.image.load("./img/star.png")
        img = pygame.transform.scale(img,[20,20])
        self.screen.blit(img,[690+num,8])   
    def print_game_over(self):
        font= pygame.font.SysFont('Calibri', 45)
        text = font.render("Game Over", False, self.white)
        self.screen.blit(text,[300,300])
        #pygame.display.flip()
    def print_heart(self,text):
        img = pygame.image.load(text)
        img = pygame.transform.scale(img,[20,20])
        self.screen.blit(img,[10,8])
        
    def level(self):
        if self.score <= 100:
            self.flag == True
    
    def quit(self):
        print(self.clock.get_fps())
        
        pygame.quit()
