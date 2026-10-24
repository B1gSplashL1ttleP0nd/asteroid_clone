from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0  # Track the time of the last shot
        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen: pygame.Surface) -> None:
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt  # Update the shot timer

        if keys[pygame.K_a]:
            self.rotate(-dt)
            # ?
        if keys[pygame.K_d]:
            self.rotate(dt)
            # ?
        if keys[pygame.K_w]:
            self.move(dt)
            # ?
        if keys[pygame.K_s]:
            self.move(-dt)
            # ?
        if keys[pygame.K_SPACE]:
            self.shoot()
            # ?

    def shoot(self) -> "Shot":
        if self.shot_timer > 0:
            return  # Prevent shooting if the cooldown hasn't passed
        self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS  # Reset the shot timer
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    