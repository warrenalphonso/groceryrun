import pyglet 
# Set resource path to assets/ - this is relative to main.py, NOT game/resources.py
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

def center(im):
    # Moves image anchor point to middle, instead of lower left corner 
    im.anchor_x = im.width // 2
    im.anchor_y = im.height // 2

home_background = pyglet.resource.image("home_background.png")

# character_rough.png is 64 x 64
character_image = pyglet.resource.image("full_main_character1.png")
character_image.width = 200 
character_image.height = 200
center(character_image)
