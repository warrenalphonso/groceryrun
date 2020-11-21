import pyglet
# Set resource path to assets/ 
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

# home_background.png is 2457 x 1397
width = 2457 // 2
height = 1397 // 2
window = pyglet.window.Window(width, height)
home_background = pyglet.resource.image("home_background.png")
home_background.width = width 
home_background.height = height

@window.event 
def on_draw():
    window.clear()
    home_background.blit(0,0)

pyglet.app.run()