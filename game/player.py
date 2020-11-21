from game import constants
import pyglet
from pyglet.window import key
import pymunk

from . import entity, resources

jump_time = 1


class Player(entity.Entity):
    def __init__(self, *args, **kwargs):
        # Trying to get Pymunk working: https://stackoverflow.com/q/11370652/13697995
        mass = 91
        radius = 14
        inertia = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, inertia)
        self.body.position = 300, 400
        self.shape = pymunk.Circle(self.body, radius)

        self.stand_right = resources.fat_man_right
        self.stand_left = resources.fat_man_left
        super().__init__(img=self.stand_right, *args, **kwargs)
        self.keys = {"facing": "right", "move": False, "jump": 0}
        self.speed = 400
        self.jump = resources.fat_man_jump
        # Walking animations
        self.walking_left = resources.fat_man_walking_left
        self.walking_right = resources.fat_man_walking_right
        # Resources
        # self.money = 0
        self.toilet_paper = 0
        self.pills = 0
        # Grocery
        self.grocery = False

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT or symbol == key.A:
            self.keys["facing"] = "left"
            self.keys["move"] = True
            self.image = self.walking_left
        elif symbol == key.RIGHT or symbol == key.D:
            self.keys["facing"] = "right"
            self.keys["move"] = True
            self.image = self.walking_right
        elif (symbol == key.UP or symbol == key.W) and self.keys["jump"] == 0:
            self.keys["jump"] = jump_time
        elif symbol == key.SPACE:  # Only let them go if they're by the door or exit...
            if not self.grocery and self.x < constants.DOOR_MAX_X:
                self.grocery = True
            elif self.grocery:
                self.grocery = False

    def on_key_release(self, symbol, modifiers):
        if (symbol == key.LEFT or symbol == key.A) and self.keys["facing"] == "left":
            self.keys["move"] = False
        elif (symbol == key.RIGHT or symbol == key.D) and self.keys["facing"] == "right":
            self.keys["move"] = False

    def update(self, dt):
        super(Player, self).update(dt)
        self.x = self.shape.body.position.x
        self.y = self.shape.body.position.y
        if self.keys["move"]:
            if self.keys["facing"] == "left":
                self.body.velocity = (-self.speed, self.body.velocity.y)
            else:
                self.body.velocity = (self.speed, self.body.velocity.y)
        else:
            self.body.velocity = (0, self.body.velocity.y)

        if self.keys["jump"] > jump_time / 2:
            self.image = self.jump
            self.body.velocity = (self.body.velocity.x, self.speed *
                                  ((self.keys["jump"] - jump_time / 2) / (jump_time / 2))**2)
            self.keys["jump"] -= dt
        elif self.keys["jump"] > 0:
            self.image = self.jump
            self.body.velocity.y = -self.speed * \
                (self.keys["jump"] / (jump_time / 2))**2
            self.keys["jump"] -= dt
        else:
            if not self.keys["move"]:
                if self.keys["facing"] == "left":
                    self.image = self.stand_left
                else:
                    self.image = self.stand_right
            else:
                if self.keys["facing"] == "left":
                    # Must do this because can't repeatedly set walking animation or it'll be still
                    if self.image != self.walking_left:
                        self.image = self.walking_left
                else:
                    if self.image != self.walking_right:  # Same as above
                        self.image = self.walking_right
            self.keys["jump"] = 0
