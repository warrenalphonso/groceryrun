import arcade
from game import constants, HomeView


class LoseView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/game_over.gif")
        arcade.set_viewport(0, constants.WIDTH, 0, constants.HEIGHT)
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        l, r, b, t = self.window.get_viewport()
        self.texture.draw_sized(l + (r - l) / 2, constants.HEIGHT / 2,
                                constants.WIDTH, constants.HEIGHT)

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.reset_game()
        start_view = HomeView.HomeView()
        self.window.show_view(start_view)
