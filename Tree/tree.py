import pygame
import pygame.gfxdraw
import pygame.draw
import math

pygame.init()

xx = 800
yy = 800
r = 2/3
dTheta = math.pi/6

screen = pygame.display.set_mode([xx, yy])

def draw_line(screen, x, y, length, theta): 
    if (length <=0.1):
        return
    x2 = x - length*math.cos(theta)
    y2 = y - length*math.sin(theta)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x2, y2))
    draw_line(screen, x2, y2, length*r, theta-dTheta )
    draw_line(screen, x2, y2, length*r, theta+dTheta)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    screen.fill((255, 255, 255))
    draw_line(screen, xx/2, yy, 150, math.pi/2)
    pygame.display.flip()

pygame.quit()