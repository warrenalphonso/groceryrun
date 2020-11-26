import arcade
from game import constants, GameView


class HomeView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        # Reset the viewport, necessary if we have a scrolling game
        arcade.set_viewport(0, self.window.w, 0, self.window.h)
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        logo = arcade.load_texture("assets/logo.png")
        logo.draw_sized(self.window.w / 2, self.window.h * 2 / 3,
                        self.window.w / 2, self.window.h / 2)
        start_blank = arcade.load_texture("assets/normal_start.png")
        start_blank.draw_sized(self.window.w / 2, self.window.h * 1 / 5,
                               self.window.w / 4, self.window.h / 6)

    def on_mouse_press(self, x, ywd, button, modifiers):
        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)
