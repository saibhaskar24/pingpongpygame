import pygame
pygame.init()
HEIGHT = 600
WIDTH = 1200
BORDER =20
VELOCITY = 1

class Ball:
    RADIUS = 10

    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self,colour):
        global screen
        pygame.draw.circle(screen,colour,(self.x,self.y),self.RADIUS)

    def update(self):
        self.x +=self.vx
        self.y +=self.vy


screen = pygame.display.set_mode((WIDTH,HEIGHT))
col = pygame.Color('white')
pygame.draw.rect(screen,col,pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen,col,pygame.Rect((0,0,BORDER,HEIGHT)))
pygame.draw.rect(screen,col,pygame.Rect((0,HEIGHT - BORDER,WIDTH,BORDER)))

ballplay = Ball(WIDTH-Ball.RADIUS,HEIGHT//2,-VELOCITY,0)

ballplay.show(col)
pygame.display.flip()
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        pygame.quit()
