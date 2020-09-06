import pygame
pygame.init()
HEIGHT = 600
WIDTH = 1200
BORDER =20
VELOCITY = 1
FRAMERATE = 1000

screen = pygame.display.set_mode((WIDTH,HEIGHT))
fcol = pygame.Color('white')
bcol = pygame.Color('black')
pygame.draw.rect(screen,fcol,pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen,fcol,pygame.Rect((0,0,BORDER,HEIGHT)))
pygame.draw.rect(screen,fcol,pygame.Rect((0,HEIGHT - BORDER,WIDTH,BORDER)))

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
        global  fcol,bcol
        newx = self.x +self.vx
        newy = self.y +self.vy
        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT- BORDER - self.RADIUS:
            self.vy = -self.vy
        elif newx+self.RADIUS > WIDTH - Paddle.WIDTH and abs(newy-paddle.y) < Paddle.HEIGHT//2:
            self.vx = -self.vx
        else:
            self.show(bcol)
            self.x+=self.vx
            self.y+=self.vy
            self.show(fcol)

class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self,y):
        self.y = y
    def show(self,colour):
        global screen
        pygame.draw.rect(screen,colour,pygame.Rect((WIDTH-self.WIDTH,self.y-self.HEIGHT//2,self.WIDTH,self.HEIGHT)))

    def update(self):
        global fcol, bcol
        self.show(bcol)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fcol)


ballplay = Ball(WIDTH-Ball.RADIUS,HEIGHT//2,-VELOCITY,-VELOCITY)
ballplay.show(fcol)
paddle = Paddle(HEIGHT//2)
paddle.show(fcol)
clock = pygame.time.Clock()
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        pygame.quit()
    clock.tick(FRAMERATE)
    pygame.display.flip()
    paddle.update()
    ballplay.update()
