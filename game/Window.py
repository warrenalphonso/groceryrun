import arcade
from game import constants, sounds


class Window(arcade.Window):
    def __init__(self):
        super().__init__(constants.WIDTH, constants.HEIGHT, constants.TITLE)
        self.reset_game()
        self.music_on = True
        self.fx_on = True

        sounds.music.play(volume=.03)

    def on_update(self, dt):
        # Loop sound
        if self.music_on and sounds.music.is_complete():
            sounds.music.play(volume=.03)

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
                    "assets/items/toilet_paper.png", constants.SPRITE_SCALING_TILES / 2)
                TP.center_x = x
                TP.center_y = 200
                self.item_list.append(TP)
        self.score = 0
        self.goal = 15
