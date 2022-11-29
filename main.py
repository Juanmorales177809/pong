import pygame
from pong_POO_2 import Pong
from player import Player
from ball import Ball



def main_loop(juego,player,ball):
    done = False
    global speed_level
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect_change_x = -6
                elif event.key == pygame.K_RIGHT:
                    player.rect_change_x = 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.rect_change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.rect_change_y = 0
        
        juego.screen.fill(juego.black)
        player.rect_x += player.rect_change_x
        player.rect_y += player.rect_change_y
        ball.ball_x += ball.ball_change_x
        ball.ball_y += ball.ball_change_y
        ball.handles_ball(player.rect_x)
        ball.draw_ball(juego.screen,juego.white)
        player.drawrect(juego)
        center = [730,10]
        speed_level= lebel(ball.score)
        juego.clock.tick(speed_level)
        juego.print_score(ball.score,center,15)
        juego.print_lifes(ball.lifes)
        game_over(ball.lifes,ball.score)
        
        
        pygame.display.flip()
        
        
        # juego.quit()
def game_over(lifes, score):
    if lifes == 0:
        juego.print_game_over()
        juego.print_score(ball.score,[300,250],45)
        juego.print_heart("sin_cora.png")
        
    elif lifes == 3:
        juego.print_heart("cora.png")
    elif lifes == 2:
        juego.print_heart("medio_cora.png")
    elif lifes == 1:
        juego.print_heart("casi_sin_cora.png")
    
    
def lebel(score):
    if score < 10:
        speed_level = 60
    if score >= 10:
        juego.print_star(-30)
        speed_level =70

    if score >=20 and score>10:
        juego.print_star(-10)
        speed_level =100
    if score >=30 and score>20:
        juego.print_star(10)
        speed_level =150
    return speed_level
if "__main__"== __name__:
    juego = Pong()
    player = Player()
    ball = Ball()
    main_loop(juego,player,ball)