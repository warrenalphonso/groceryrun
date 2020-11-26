import arcade
from game import views


def main():
    window = views.CustomWindow()
    start_view = views.HomeView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
