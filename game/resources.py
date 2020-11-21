import pyglet 
# Set resource path to assets/ - this is relative to main.py, NOT game/resources.py
pyglet.resource.path = ['assets']
pyglet.resource.reindex()

def center(im):
    # Moves image anchor point to middle, instead of lower left corner 
    im.anchor_x = im.width // 2
    im.anchor_y = im.height // 2

home_background = pyglet.resource.image("home_background.png")

# fat_man_right.png is 64 x 64
fat_man_width = 200 
fat_man_height = 200
fat_man_frame_delay = 0.1

fat_man_right = pyglet.resource.image("fat_man_right.png")
fat_man_right.width = fat_man_width 
fat_man_right.height = fat_man_height
center(fat_man_right)

fat_man_left = pyglet.resource.image("fat_man_left.png")
fat_man_left.width = fat_man_width 
fat_man_left.height = fat_man_height
center(fat_man_left)

fat_man_jump = pyglet.resource.image("fat_man_jump.png")
fat_man_jump.width = fat_man_width
fat_man_jump.height = fat_man_height
center(fat_man_jump)

# walking 
fat_man_walking_right_images = []
for fname in ["1", "2", "3", "4", "5", "6", "7"]:
    image = pyglet.resource.image("fat_man_walking_right/{0}.png".format(fname))
    image.width = fat_man_width
    image.height = fat_man_height 
    center(image)
    fat_man_walking_right_images.append(image)
fat_man_walking_right = pyglet.image.Animation.from_image_sequence(fat_man_walking_right_images, fat_man_frame_delay, True)

fat_man_walking_left_images = []
for fname in ["1", "2", "3", "4", "5", "6", "7"]:
    image = pyglet.resource.image("fat_man_walking_left/{0}.png".format(fname))
    image.width = fat_man_width
    image.height = fat_man_height 
    center(image)
    fat_man_walking_left_images.append(image)
fat_man_walking_left = pyglet.image.Animation.from_image_sequence(fat_man_walking_left_images, fat_man_frame_delay, True)
