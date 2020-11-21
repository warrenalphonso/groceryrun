import pyglet
from . import resources

def number_to_two_digit_string(num):
    if num < 0:
        return "00"
    elif num < 10:
        return "0" + str(num)
    elif num < 100:
        return str(num)
    else:
        return "99"

# def draw_resource_amounts(image_and_scores, margin_top, margin_in_between):
#     margin_left = 0
#     for image, score in image_and_scores:
#         margin_left += margin_in_between 
#         margin_left += image.width // 2
#         image.blit(margin_left, margin_top)
#         label = pyglet.text.Label(number_to_two_digit_string(score),
#                           font_name="Times New Roman",
#                           font_size=22,
#                           x=margin_left, y=margin_top,
#                           anchor_x='center', anchor_y='center')
#         label.draw()
#         margin_left += image.width // 2 
margin_in_between = 40 
margin_top = 50

def draw_resource_amounts(window_height, toilet_paper_amount, pills_amount):
    margin_left = 0 
    # TP
    margin_left += margin_in_between 
    margin_left += resources.toilet_paper_amount.width // 2
    resources.toilet_paper_amount.blit(margin_left, window_height - margin_top)
    label = pyglet.text.Label(number_to_two_digit_string(toilet_paper_amount), 
        font_name="Times New Roman", font_size=22, color=(0, 0, 0, 200),
        x=margin_left-20, y=window_height - margin_top, 
        anchor_x="center", anchor_y="center")
    label.draw() 
    margin_left += resources.toilet_paper_amount.width // 2
    # Pills 
    margin_left += margin_in_between 
    margin_left += resources.pills_amount.width // 2
    resources.pills_amount.blit(margin_left, window_height - margin_top)
    label = pyglet.text.Label(number_to_two_digit_string(pills_amount), 
        font_name="Times New Roman", font_size=22, color=(0, 0, 0, 200),
        x=margin_left-10, y=window_height - margin_top, 
        anchor_x="center", anchor_y="center")
    label.draw() 
    margin_left += resources.pills_amount.width // 2
 