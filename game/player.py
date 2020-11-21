from pyglet.window import key

from . import entity, resources 

class Player(entity.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.character_image, *args, **kwargs)
        self.speed = 200

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT or symbol == key.A:
            self.keys['left'] = True
        elif symbol == key.RIGHT or symbol == key.D:
            self.keys['right'] = True
        elif symbol == key.UP or symbol == key.W:
            self.keys['up'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT or symbol == key.A:
            self.keys['left'] = False
        elif symbol == key.RIGHT or symbol == key.D:
            self.keys['right'] = False
        elif symbol == key.UP or symbol == key.W:
            self.keys['up'] = False

    def update(self, dt):
        super(Player, self).update(dt)
