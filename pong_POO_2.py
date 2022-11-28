import pygame


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
    
        
    def print_score(self,score):
        font= pygame.font.SysFont('Calibri', 15, False, False)
        text = font.render("Score = " + str(score), True, self.white)
        self.screen.blit(text,[600,100])
        pygame.display.flip()
        self.clock.tick(60)
        #score board
    def print_lifes(self, lifes):
        font= pygame.font.SysFont('Calibri', 15, False, False)
        text = font.render("Lifes = " + str(lifes), True, self.white)
        self.screen.blit(text,[600,120])
        pygame.display.flip()
        self.clock.tick(60)
    def level(self):
        if self.score <= 100:
            self.flag == True
    def quit(self):
        pygame.quit()
