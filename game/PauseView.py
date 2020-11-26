import arcade
from game import sounds, HomeView


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.window.set_mouse_visible(True)

    def on_show(self):
        pass

    # TODO: Conver to mouse click
    def on_draw(self):
        self.game_view.on_draw()
        l, r, b, t, w, h = self.window.l, self.window.r, self.window.b, self.window.t, self.window.w, self.window.h
        # Draw blue hue over screen
        arcade.draw_lrtb_rectangle_filled(
            left=l, right=r, top=t, bottom=b,
            color=arcade.color.LIGHT_SKY_BLUE + (220, ))  # Concatenate 200 for transparency
        infection = arcade.load_texture("assets/infection_symbol.png")
        infection.draw_sized(l + w / 2, h *
                             4 / 5, h / 4, h / 4)
        arcade.draw_text("PAUSED", l + w/2, h * .55,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Press ESCAPE to return to the game", l + w/2,
                         h * .45, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press ENTER to exit", l + w/2,
                         h * .35, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press M to toggle music", l + w/2,
                         h * .25, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press F to toggle sound effects", l + w/2,
                         h * .15, arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:
            self.window.reset_game()
            start_view = HomeView.HomeView()
            self.window.show_view(start_view)
        elif key == arcade.key.M:
            if self.window.music_on:
                self.window.music_on = False
                sounds.music.stop()
            else:
                self.window.music_on = True
        elif key == arcade.key.F:
            self.window.fx_on = not self.window.fx_on
