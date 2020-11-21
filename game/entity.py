# Generic entity that obeys physics. All specific entities (players, enemies)
# inherit from this. Entities are sprites.
import pyglet

from . import constants


class Entity(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0.0
        self.vy = 0.0
        self.min_x = 0
        self.max_x = constants.WIDTH

    def check_bounds(self):
        if self.x + self.width // 2 > self.max_x:
            self.x = self.max_x - self.width // 2
        elif self.x - self.width // 2 < self.min_x:
            self.x = self.min_x + self.width // 2

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.check_bounds()
