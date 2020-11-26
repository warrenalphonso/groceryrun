import arcade
from game import constants, sounds

WIDTH = 16 * constants.SPRITE_SIZE
HEIGHT = 12 * constants.SPRITE_SIZE
TITLE = "Grocery Run"


class Window(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.update_window()
        self.reset_game()
        self.music_on = True
        self.fx_on = True
        sounds.music.play(volume=.03)

    # def on_resize(self, width, height):
    #     self.update_window()

    def on_update(self, dt):
        # Loop sound
        if self.music_on and sounds.music.is_complete():
            sounds.music.play(volume=.03)
        self.update_window()

    # def on_key_press(self, key, modifiers):
    #     if key == arcade.key.F:
    #         self.set_fullscreen(not self.fullscreen)
    #         w, h = self.get_size()
    #         print("GET_SIZE WIDTH: ", w)
    #         print("SELF WIDTH: ", w)
    #         self.set_viewport(0, w, 0, h)
    # TODO: This should be associated with a level, not the window.

    def reset_game(self):
        self.hits_left = 4
        self.item_list = arcade.SpriteList()
        for i, x in enumerate(range(150, int(constants.LEVEL_WIDTH), int(constants.LEVEL_WIDTH / 20))):
            if i == 2:
                continue
            elif i == 12:
                continue
            else:
                TP = arcade.Sprite(
                    "assets/items/toilet_paper.png", constants.SCALING_TILES / 2)
                TP.center_x = x
                TP.center_y = 200
                self.item_list.append(TP)
        self.score = 0
        self.goal = 15

    def update_window(self):
        l, r, b, t = arcade.get_viewport()
        w, h = r - l, t - b
        self.l = l
        self.r = r
        self.b = b
        self.t = t
        self.w = w
        self.h = h
