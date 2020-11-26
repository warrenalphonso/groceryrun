import arcade
from game import Window, HomeView


def main():
    window = Window.Window()
    start_view = HomeView.HomeView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
