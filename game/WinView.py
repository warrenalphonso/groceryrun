import arcade
from game import GameView


class WinView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You win! Click to Play Again!", self.window.l + self.window.w / 2, self.window.h / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        self.window.reset_game()
        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)
