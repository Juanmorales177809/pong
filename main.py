import pygame
from pong_POO_2 import Pong
from player import Player
from ball import Ball



def main_loop(juego,player,ball):
    done = False
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
        juego.print_score(ball.score)
        juego.print_lifes(5)
            
if "__main__"== __name__:
    juego = Pong()
    player = Player()
    ball = Ball()
    main_loop(juego,player,ball)    