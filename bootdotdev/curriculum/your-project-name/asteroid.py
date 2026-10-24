import random
from logger import log_event
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, int(self.radius), LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = self.velocity.rotate(angle) * 1.2
            new_asteroid2.velocity = self.velocity.rotate(-angle) * 1.2
            
