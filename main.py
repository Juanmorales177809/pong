import pygame
from pong_POO_2 import Pong
from player import Player
from ball import Ball
from bonus import Bonus
import time
import random



def main_loop(juego,player,ball,life,star,no_life):
    contador = 0
    done = False
    global speed_level
    
    while not done:
        contador+=1
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
        if ball.lifes > 0:
            ball.ball_x += ball.ball_change_x
            ball.ball_y += ball.ball_change_y
        else:
            ball.ball_x = 400
            ball.ball_y = 150
        
        
        life.handles_bonus(player.rect_x)
        life.draw_life(juego.screen)
        if contador > 100:
            star.handles_bonus(player.rect_x)
            star.draw_score(juego.screen)
        if contador > 200:
            life.handles_bonus(player.rect_x)
            life.draw_life(juego.screen)
        if contador > 400:
            no_life.handles_bonus(player.rect_x)
            no_life.draw_lost_life(juego.screen)
        if life.bandera:
            ball.lifes +=1
            life.bandera = False
        if no_life.bandera:
            ball.lifes -=1
            no_life.bandera = False
        if star.bandera:
            ball.score +=1
            star.bandera = False
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
        juego.print_heart("./img/sin_cora.png")
        
        
    elif lifes == 3:
        juego.print_heart("./img/cora.png")
    elif lifes == 2:
        juego.print_heart("./img/medio_cora.png")
    elif lifes == 1:
        juego.print_heart("./img/casi_sin_cora.png")
    
    
def lebel(score):
    if score < 10:
        speed_level = 60
    elif score >= 10 and score < 20:
        juego.print_star(-30)
        speed_level =70

    elif score >=20 and score<30:
        juego.print_star(-10)
        speed_level =100
    elif score >=30 :
        juego.print_star(10)
        speed_level =150
    return speed_level
if "__main__"== __name__:
    juego = Pong()
    player = Player()
    ball = Ball()
    life = Bonus()
    star = Bonus()
    no_life = Bonus()
    main_loop(juego,player,ball,life,star,no_life)