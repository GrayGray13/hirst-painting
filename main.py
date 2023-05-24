import random as r
import turtle
import turtle as t

import colorgram

t.colormode(255)
ted_the_turtle = t.Turtle()
ted_the_turtle.shape("turtle")
ted_the_turtle.speed(0)
ted_the_turtle.hideturtle()

colors_list = [(55, 108, 150), (226, 200, 108), (136, 86, 58), (223, 139, 64), (197, 144, 172), (144, 180, 206),
               (139, 81, 106), (209, 89, 70), (232, 225, 197), (134, 183, 135), (188, 78, 124), (69, 102, 87),
               (65, 155, 88), (50, 155, 196), (227, 235, 233), (132, 134, 73), (183, 191, 202), (229, 219, 224),
               (77, 55, 33), (213, 178, 192), (4, 53, 104), (21, 67, 122), (179, 25, 16), (117, 42, 58),
               (111, 124, 157), (220, 178, 170), (175, 202, 185), (47, 74, 61), (84, 62, 40)]


# Uncomment this section to use your own image and delete color_list
# ================================================================ #
# colorgram_list = colorgram.extract('image.jpg', 30)
# for color in colorgram_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
#
# print(colors_list)
# ================================================================ #


def draw_hirst(hirst_turtle):
    y_axis = 0
    hirst_turtle.goto(0, y_axis)
    for i in range(100):
        if i % 10 == 0 and i != 0:
            y_axis += 50
            hirst_turtle.goto(0, y_axis)
        hirst_turtle.dot(30, r.choice(colors_list))
        hirst_turtle.up()
        hirst_turtle.forward(50)


draw_hirst(ted_the_turtle)
screen = t.Screen()
screen.exitonclick()
