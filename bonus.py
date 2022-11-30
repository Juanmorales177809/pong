import pygame
import random



class Bonus:
    def __init__(self):
        self.life_x = random.randrange(600)
        self.life_y = 50
        self.life_speed = [0, 8]
        self.life_change_x = 5
        self.life_change_y = 5
        self.score_x = 50
        self.score_y = 50
        self.score_change_x = 5
        self.score_change_y = 5
        self.lost_life_x = 50
        self.lost_life_y = 50
        self.lost_life_change_x = 5
        self.lost_life_change_y = 5
        self.moves = None
    
    
    def draw_life(self,screen,color):
        
        life = pygame.image.load("./img/cora.png")
        life = pygame.transform.scale(life,[20,20])
        moves = life.get_rect()
        moves.move_ip(self.life_x,self.life_y)
        moves.move(self.life_speed)
        
    def move_bonus(self):
        self.moves.move(self.life_speed)
        # pygame.draw.circle(screen,color,(self.life_x,self.life_y),7)
        
        # screen.blit(life,(self.life_x,self.life_y),7)
    def draw_score(self):
        life = pygame.image.load("./img/star.png")
        life = pygame.transform.scale(life,[20,20])
        self.screen.blit(life,[random.randint(10,700),8])
    def draw_lost_life(self):
        life = pygame.image.load("./img/sin_cora.png")
        life = pygame.transform.scale(life,[20,20])
        self.screen.blit(life,[random.randint(10,700),8])
    def handles_bonus(self,rect_x):
        if self.life_y >600:
            self.life_y = 600
            self.life_change_y = self.life_y*-1
        elif self.life_y < 0:
            self.life_y = 0
            self.life_change_y = self.life_y*-1
        elif self.life_x<0:
            self.life_x=0
            self.life_change_x = self.life_change_x * -1
        elif self.life_x>785:
            self.life_x=785
            self.life_change_x = self.life_change_x * -1