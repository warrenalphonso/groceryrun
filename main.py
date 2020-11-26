import arcade
from game import CustomWindow, HomeView


def main():
    window = CustomWindow.CustomWindow()
    start_view = HomeView.HomeView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
