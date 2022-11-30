import pygame


class Pong:
    def __init__(self):
        self.size = (800,600)
        self.rect_x = 400 #Starting coordinates of the paddle
        self.rect_y = 580
        self.rect_change_x = 0 #initial speed of the paddle
        self.rect_change_y = 0
        self.ball_x = 50#initial position of the ball
        self.ball_y = 50
        self.ball_change_x = 5#speed of the ball
        self.ball_change_y = 5#speed of the ball
        self.score = 0
        self.done = False
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("pong")#Initializing the display window
        self.clock=pygame.time.Clock()
    
        
    def drawrect(self):#draws the paddle. Also restricts its movement between the edges of the window.
        if self.rect_x <= 0:
            self.rect_x = 0
        if self.rect_x >= 699:
            self.rect_x = 699    
        pygame.draw.rect(self.screen,self.red,[self.rect_x,self.rect_y,100,20])
#game's main loop 
    def main_loop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rect_change_x = -6
                    elif event.key == pygame.K_RIGHT:
                        self.rect_change_x = 6
                    # elif event.key == pygame.K_UP:
                    #     self.rect_change_y = -6
                    # elif event.key == pygame.K_DOWN:
                    #     self.rect_change_y = 6           
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.rect_change_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.rect_change_y = 0            
            self.screen.fill(self.black)
            self.rect_x += self.rect_change_x
            self.rect_y += self.rect_change_y
            self.ball_x += self.ball_change_x
            self.ball_y += self.ball_change_y
            self.handles_ball()
    
    def handles_ball(self):#this handles the movement of the ball.
        if self.ball_x<0:
            self.ball_x=0
            self.ball_change_x = self.ball_change_x * -1
        elif self.ball_x>785:
            self.ball_x=785
            self.ball_change_x = self.ball_change_x * -1
        elif self.ball_y<0:
            self.ball_y=0
            self.ball_change_y = self.ball_change_y * -1
        elif self.ball_x>self.rect_x and self.ball_x<self.rect_x+100 and self.ball_y==565:
            self.ball_change_y = self.ball_change_y * -1
            self.score = self.score + 1
        elif self.ball_y>600:
            self.ball_change_y = self.ball_change_y * -1
            self.score = 0                        
        pygame.draw.rect(self.screen,self.white,[self.ball_x,self.ball_y,15,15])
        
        self.drawrect()
        self.print_score()
        #drawball(screen,ball_x,ball_y)
        
    def print_score(self):
        font= pygame.font.SysFont('Calibri', 15, False, False)
        text = font.render("Score = " + str(self.score), True, self.white)
        self.screen.blit(text,[600,100]) 
        pygame.display.flip() 
        self.clock.tick(60) 
        #score board
    def quit(self):
        pygame.quit()
            
        
if "__main__"==__name__:
    juego = Pong()                
    juego.main_loop()
    juego.quit()
    
 