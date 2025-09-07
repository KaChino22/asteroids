import pygame
import random
from constants import *

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x,y,radius) 
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(angle) * 1.2
            vel2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = vel1
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = vel2
        self.kill()
