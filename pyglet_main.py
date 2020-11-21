from game.constants import WIDTH
import pyglet
from pyglet.window import key
from pyglet.gl import *
import pymunk

from game import resources, player, draw, constants

main_batch = pyglet.graphics.Batch()

# home_background.png is 2457 x 1397
window = pyglet.window.Window(constants.WIDTH, constants.HEIGHT)

space = pymunk.Space()
space.gravity = (0.0, -1000.)

main_player = player.Player(x=400, y=300, batch=main_batch)
window.push_handlers(main_player)
space.add(main_player.body, main_player.shape)

# Floor
floor = pymunk.Segment(space.static_body, (0, 100), (constants.WIDTH, 100), 3)
space.add(floor)

# Door
label = pyglet.text.Label("",
                          font_name=constants.FONT,
                          font_size=34, color=(0, 0, 0, 250),
                          x=window.width//2, y=80,
                          anchor_x='center', anchor_y='center')


def update(dt):
    main_player.update(dt)
    space.step(dt)
    # Check if player is at door, then display text
    if main_player.x < constants.DOOR_MAX_X:
        label.text = "To go on a grocery run, press SPACE"
    else:
        label.text = ""
    # Check if player wants to load grocery
    if main_player.grocery:
        print("GROCERY")
        resources.home_background.image = pyglet.resource.image(
            "background_room_new.png")
        window.clear()
        resources.home_background.blit(0, 0)
    else:
        print("HOME")


@window.event
def on_draw():
    window.clear()
    # Scale pixel art as per: https://gamedev.stackexchange.com/a/57114
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glEnable(GL_BLEND)  # From https://stackoverflow.com/a/46048254/13697995
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    resources.home_background.blit(0, 0)
    resources.TV.blit(constants.WIDTH - 300, constants.HEIGHT - 200)
    resources.news_phone.blit(constants.WIDTH - 300, constants.HEIGHT - 200)

    draw.draw_resource_amounts(main_player.toilet_paper, main_player.pills)

    label.draw()

    main_batch.draw()


# 120 FPS
pyglet.clock.schedule_interval(update, 1 / 120.0)
pyglet.app.run()
