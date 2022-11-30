import sys, pygame
import time
import random


#Inicializar motor de graficos
pygame.init()
#Defino tamano de ventana
size = 800, 600
screen = pygame.display.set_mode(size)
#Cambiar titulo de la ventana
pygame.display.set_caption("Pong")
#Inicializar variables
width, height = 800, 600
speed = [10, 0]
white = 255, 255, 255

#Crear objeto
ball = pygame.image.load("./img/ball2.png")
#ball = pygame.transform.scale(ball, (40,40))
rectangulo = ball.get_rect()
rectangulo.move_ip(400,random.randrange(300))

#Bucle del juego

run= True
while run:
    pygame.time.delay(10)
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT: run = False

    rectangulo = rectangulo.move(speed)
    ball = pygame.image.load("./img/ball2.png")
    
    



    # if rectangulo.left < 0 :
    #     speed[0] = -speed[0]
    #     ball = pygame.image.load("./img/mario2.png")
    #     pygame.time.delay(8)
    #     ball = pygame.image.load("./img/marioCamina.png")
    # if rectangulo.right > width:
    #     speed[0] = -speed[0]
    #     ball = pygame.image.load("./img/marioGiraDer.png")
    #     ball = pygame.image.load("./img/marioCamina-.png")



    if rectangulo.top < 0 or rectangulo.bottom > height:
        speed[1] = -speed[1]
    screen.fill(white)
    screen.blit(ball, rectangulo)
    pygame.display.flip()
pygame.quit()