import pygame




class Ball:
    def __init__(self):
        self.ball_x = 50#initial position of the ball
        self.ball_y = 50
        self.ball_change_x = 5#speed of the ball
        self.ball_change_y = 5#speed of the ball
        self.score =0
        self.lifes = 3
    
    def handles_ball(self,rect_x):#this handles the movement of the ball.
        
        if self.ball_x<0:
            self.ball_x=0
            self.ball_change_x = self.ball_change_x * -1
        elif self.ball_x>785:
            self.ball_x=785
            self.ball_change_x = self.ball_change_x * -1
        elif self.ball_y<0:
            self.ball_y=0
            self.ball_change_y = self.ball_change_y * -1
        elif self.ball_x>rect_x and self.ball_x<rect_x+100 and self.ball_y==575:
            self.ball_change_y = self.ball_change_y * -1
            self.score +=1
        elif self.ball_y>600:
            self.ball_change_y = self.ball_change_y * -1
            self.score -= 1
            self.lifes -=1
            
    def draw_ball(self,screen,color):
        pygame.draw.circle(screen,color,(self.ball_x,self.ball_y),7)
    
    
        