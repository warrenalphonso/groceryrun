import pyglet
# Set resource path to assets/ - this is relative to main.py, NOT game/resources.py
pyglet.resource.path = ['assets']
pyglet.resource.reindex()


def center(im):
    # Moves image anchor point to middle, instead of lower left corner
    im.anchor_x = im.width // 2
    im.anchor_y = im.height // 2


home_background = pyglet.resource.image("home_background.png")

# AMOUNTS

# 62 x 27
money_amount = pyglet.resource.image("amounts/money_amount.png")
money_amount.width = 120
money_amount.height = 27 / 62 * money_amount.width
center(money_amount)
# 77 x 32
toilet_paper_amount = pyglet.resource.image("amounts/toilet_paper_amount.png")
toilet_paper_amount.width = 120
toilet_paper_amount.height = 32 / 77 * toilet_paper_amount.width
center(toilet_paper_amount)
# 77 x 32
pills_amount = pyglet.resource.image("amounts/pills_amount.png")
pills_amount.width = 120
pills_amount.height = 32 / 77 * pills_amount.width
center(pills_amount)

# TV

# 124 x 69
TV = pyglet.resource.image("tv/TV.png")
TV.width = 300
TV.height = 69 / 124 * TV.width
center(TV)

# 128 x 73, but make it same as above
TV_highlight = pyglet.resource.image("tv/TV_highlight.png")
TV_highlight.width = TV.width
TV_highlight.height = TV.height
center(TV_highlight)

# 118 x 60
news_phone = pyglet.resource.image("tv/news_phone.png")
news_phone.width = 118 / 124 * TV.width
news_phone.height = 60 / 69 * TV.height
center(news_phone)

news_stimulus = pyglet.resource.image("tv/news_stimulus.png")
news_stimulus.width = news_phone.width
news_stimulus.height = news_phone.height
center(news_stimulus)

news_virus = pyglet.resource.image("tv/news_virus.png")
news_virus.width = news_phone.width
news_virus.height = news_phone.height
center(news_virus)

# ENTITIES

# fat_man_right.png is 64 x 64f
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
    image = pyglet.resource.image(
        "fat_man_walking_right/{0}.png".format(fname))
    image.width = fat_man_width
    image.height = fat_man_height
    center(image)
    fat_man_walking_right_images.append(image)
fat_man_walking_right = pyglet.image.Animation.from_image_sequence(
    fat_man_walking_right_images, fat_man_frame_delay, True)

fat_man_walking_left_images = []
for fname in ["1", "2", "3", "4", "5", "6", "7"]:
    image = pyglet.resource.image("fat_man_walking_left/{0}.png".format(fname))
    image.width = fat_man_width
    image.height = fat_man_height
    center(image)
    fat_man_walking_left_images.append(image)
fat_man_walking_left = pyglet.image.Animation.from_image_sequence(
    fat_man_walking_left_images, fat_man_frame_delay, True)
