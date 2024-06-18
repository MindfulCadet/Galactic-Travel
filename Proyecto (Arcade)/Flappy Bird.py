#Libraries
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
name = pygame.display.set_caption("Galactic Travel")
clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('assets/background/travel-bg.jpeg'),(800,400))


#Game variables
running = True
dt = 0
game_speed = 2
frequency = 2000
last_pipe = pygame.time.get_ticks() - frequency
start = False
game_over = False

class Message:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y


class Pajaro:
    #Constructor function for the class
    def __init__(self, posicion, player_image):
        self.pos_inicial = posicion
        self.aceleracion = 0.0
        self.velocidad = 0.0
        self.pressed = False
        self.player_image_surface = pygame.transform.scale(pygame.image.load(player_image),(80,40))
        self.player_image_rect = pygame.Surface.get_rect(self.player_image_surface, topleft = self.pos_inicial)

    
    def pajaro_movimiento(self, keys):

        if keys[pygame.K_z] == False:
            self.pressed = False

        if keys[pygame.K_z] and self.pressed == False:
          self.velocidad = -500
          self.pressed = True

    #Defines the movement of the playable character
    def posicion(self):

        self.pajaro_movimiento(pygame.key.get_pressed()) 

        if start == True:
           self.aceleracion = 1500
           self.pos_inicial.y += self.velocidad*dt + (self.aceleracion*dt**2)*0.5
           self.velocidad += self.aceleracion*dt
        screen.blit(self.player_image_surface,self.pos_inicial)

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, image, x, y, type):

        pygame.sprite.Sprite.__init__(self)

        if type == 1:
           self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]

        if type == 2:
           self.image = pygame.transform.scale(pygame.image.load(image), (150, 150))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]

        if type == 3:
           self.image = pygame.transform.scale(pygame.image.load(image), (250, 250))
           self.rect = self.image.get_rect()
           self.rect.topleft = [x,y]

    def update(self):
        self.rect.x -= game_speed

jugador = Pajaro(pygame.Vector2(200,200),'assets/character/ufo.webp')
asteroid_group = pygame.sprite.Group()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))

    time = pygame.time.get_ticks()

    if start == False:
        check = pygame.key.get_pressed()

        if check[pygame.K_z]:
            start = True


    if start == True and game_over == False:
        if time - last_pipe > frequency:
            pipe_height = random.randint(0, 300)
            asteroid_type = random.randint(1,3)
            obstacle_up = Obstaculos('assets/blocks/asteroid1.png', 800, 0 + pipe_height, asteroid_type )
            asteroid_group.add(obstacle_up)
            last_pipe = time
        

    jugador.posicion()
    asteroid_group.draw(screen)
    asteroid_group.update()
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()