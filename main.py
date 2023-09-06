from math import sqrt, pow, sin, cos, tan, pi, atan
from random import randint
import pygame
import sys
import time
import particle
import universe

# 1px = 1m

plist = []
WIDTH, HEIGHT = 800, 800
running = True
particle_number = 10

PS = universe.ParticleSystem()
for _ in range(10):
    p = particle.Particle(randint(0, 800), randint(0, 800), pow(10, 10), 0, 30, 7)
    plist.append(p)

def draw_particles():        
    screen.fill((0, 0, 0))
    for p in plist:
        pygame.draw.circle(screen, p.color, (p.x, p.y), p.r, 0)
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("gravity")
# time.sleep(1.5) -> useful for debugging
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    
    PS.update_particle_positions(plist)
    draw_particles()
    pygame.display.flip()

pygame.quit()
sys.exit()
