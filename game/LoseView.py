import arcade
from game import HomeView


class LoseView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/game_over.gif")
        arcade.set_viewport(0, self.window.w, 0, self.window.h)
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        l, r, b, t = arcade.get_viewport()
        self.texture.draw_sized(l + (r - l) / 2, self.window.h / 2,
                                self.window.w, self.window.h)

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.reset_game()
        start_view = HomeView.HomeView()
        self.window.show_view(start_view)
