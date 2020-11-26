import arcade
from game import constants, GameView


class HomeView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        # Reset the viewport, necessary if we have a scrolling game
        arcade.set_viewport(0, constants.WIDTH, 0, constants.HEIGHT)
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        logo = arcade.load_texture("assets/logo.png")
        logo.draw_sized(constants.WIDTH / 2, constants.HEIGHT * 2 / 3,
                        constants.WIDTH / 2, constants.HEIGHT / 2)
        start_blank = arcade.load_texture("assets/normal_start.png")
        start_blank.draw_sized(constants.WIDTH / 2, constants.HEIGHT * 1 / 5,
                               constants.WIDTH / 4, constants.HEIGHT / 6)

    def on_mouse_press(self, x, ywd, button, modifiers):
        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)
