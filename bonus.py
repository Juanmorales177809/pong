import pygame
import random



class Bonus:
    def __init__(self):
        self._x = random.randrange(0,600)
        self._y = 50
        self.changue_x = 0
        self.speed = [random.randrange(0,600), 5]
        self.bandera = False
        
    def draw_life(self,screen):
        life = pygame.image.load("./img/cora.png").convert_alpha()
        life = pygame.transform.scale(life,[20,20])
        moves = life.get_rect()
        moves.move_ip(self._x,self._y)
        moves = moves.move(self.speed)
        self.speed[1] +=1
        screen.blit(life,self.speed)
    
    def move_bonus(self):
        self.moves.move(self.life_speed)
        
    def draw_score(self,screen):
        star = pygame.image.load("./img/star.png")
        star = pygame.transform.scale(star,[20,20])
        moves = star.get_rect()
        moves.move_ip(self._x,self._y)
        moves = moves.move(self.speed)
        self.speed[1] +=1
        screen.blit(star,self.speed)
    
    def draw_lost_life(self,screen):
        life = pygame.image.load("./img/sin_cora.png").convert_alpha()
        life = pygame.transform.scale(life,[20,20])
        moves = life.get_rect()
        moves.move_ip(self._x,self._y)
        moves = moves.move(self.speed)
        self.speed[1] +=1
        screen.blit(life,self.speed)
    
    def handles_bonus(self,rect_x):
        if self.speed[1]>600:
            self.speed[1] = 600
            self.speed[1] *= -1
            self.speed[0] = random.randrange(0,600)
        elif self.speed[1] < 0:
            self.speed[1] = 0
            self.speed[1] *= -1
            self.speed[0] = random.randrange(0,600)
        elif self.speed[0]>rect_x and self.speed[0]<rect_x+100 and self.speed[1]==575:
            self.speed[1] *= -1
            self.speed[0] = random.randrange(0,600)
            self.bandera = True
            
            
        # elif self.life_x<0:
        #     self.life_x=0
        #     self.life_change_x = self.life_change_x * -1
        # elif self.life_x>785:
        #     self.life_x=785
        #     self.life_change_x = self.life_change_x * -1
        