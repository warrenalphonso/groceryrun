# Generic entity that obeys physics. All specific entities (players, enemies)
# inherit from this. Entities are sprites.
import pyglet

from . import constants


class Entity(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_x = 0
        self.max_x = constants.WIDTH

    def check_bounds(self):
        if self.shape.body.position.x + self.width // 2 > self.max_x:
            self.shape.body.position = (self.max_x - self.width // 2, self.y)
        elif self.shape.body.position.x - self.width // 2 < self.min_x:
            self.shape.body.position = (self.min_x + self.width // 2, self.y)

    def update(self, dt):
        self.check_bounds()
