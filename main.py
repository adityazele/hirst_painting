# HirstInspired: Python program mimics $1 million spot painting! 🎨

import random

import colorgram
from turtle import Turtle, Screen

image = 'image.jpg'
number_of_colors_to_be_extracted = 11
turtle_step_length = 25


def get_colors(img, num):
    colors = colorgram.extract(img, num)

    color_list = []

    pos = 0
    for _ in range(num):
        color = colors[pos]
        rgb = color.rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        rgb_tuple = (red, green, blue)
        color_list.append(rgb_tuple)
        pos += 1

    print(color_list)
    return color_list


def paint(x, y):
    tim.goto(x, y)

    num = 0
    color_list = []
    for _ in range(len(colors_list)):
        random_color = random.choice(colors_list)
        while random_color in color_list:
            random_color = random.choice(colors_list)
        color_list.append(random_color)
        tim.dot(10, random_color)
        tim.forward(turtle_step_length)
        num += 1


colors_list = get_colors(image, number_of_colors_to_be_extracted)

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')

x_cor = -(number_of_colors_to_be_extracted * turtle_step_length) / 2
y_cor = x_cor
for _ in range(len(colors_list)):
    paint(x_cor, y_cor)
    y_cor += turtle_step_length

screen.exitonclick()
