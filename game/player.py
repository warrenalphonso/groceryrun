import pyglet
from pyglet.window import key

from . import entity, resources 

jump_time = 1

class Player(entity.Entity):
    def __init__(self, *args, **kwargs):
        self.stand_right = resources.fat_man_right
        self.stand_left = resources.fat_man_left
        super().__init__(img=self.stand_right, *args, **kwargs)
        self.keys = { "facing": "right", "move": False, "jump": 0 }
        self.speed = 400
        self.jump = resources.fat_man_jump
        # Walking animations 
        self.walking_left = resources.fat_man_walking_left
        self.walking_right = resources.fat_man_walking_right

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

    def on_key_release(self, symbol, modifiers):
        if (symbol == key.LEFT or symbol == key.A) and self.keys["facing"] == "left":
            self.keys["move"] = False
        elif (symbol == key.RIGHT or symbol == key.D) and self.keys["facing"] == "right":
            self.keys["move"] = False

    def update(self, dt):
        super(Player, self).update(dt)
        if self.keys["move"]:
            if self.keys["facing"] == "left":
                self.vx = -self.speed 
            else: 
                self.vx = self.speed
        else: 
            self.vx = 0
        


        if self.keys["jump"] > jump_time / 2:
            self.image = self.jump
            self.vy = self.speed * ((self.keys["jump"] - jump_time / 2) / (jump_time / 2))**2
            self.keys["jump"] -= dt
        elif self.keys["jump"] > 0:
            self.image = self.jump
            self.vy = -self.speed * (self.keys["jump"] / (jump_time / 2))**2
            self.keys["jump"] -= dt
        else:
            if not self.keys["move"]:
                if self.keys["facing"] == "left":
                    self.image = self.stand_left
                else: 
                    self.image = self.stand_right
            else:
                if self.keys["facing"] == "left":
                    if self.image != self.walking_left: # Must do this because can't repeatedly set walking animation or it'll be still
                        self.image = self.walking_left
                else: 
                    if self.image != self.walking_right: # Same as above
                        self.image = self.walking_right
            self.vy = 0
            self.y = 300 # Just in case
            self.keys["jump"] = 0