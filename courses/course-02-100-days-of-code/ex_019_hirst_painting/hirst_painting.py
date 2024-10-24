from PIL import Image
import requests
from io import BytesIO
from turtle import Turtle, Screen
import colorgram
import random


def get_color_palette(url):
    point.hideturtle()
    point.write("Wait a little! Getting color palette...", align='Center', font=('Arial', 16, 'italic'))
    point.penup()

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    color_palette = colorgram.extract(img, 10)
    rgb_colors = []
    for color in color_palette:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    point.clear()
    point.showturtle()
    return rgb_colors


def change_color(obj):
    obj.color(random.choice(rgb_colors))


def draw_points(obj, lines=8):
    obj.penup()
    obj.goto(-400,-350)
    obj.pendown()
    obj.shape('circle')
    obj.speed('fastest')
    
    for _ in range(lines):
        for _ in range(10):
            change_color(obj)
            obj.pendown()
            obj.dot(50)
            obj.penup()
            obj.forward(100)
        obj.penup()
        obj.left(90)
        obj.forward(100)
        obj.left(90)
        obj.forward(1000)
        obj.setheading(0)


screen = Screen()
screen.colormode(255)
point = Turtle()
URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Mario_Series_Logo.svg/2560px-Mario_Series_Logo.svg.png'
rgb_colors = get_color_palette(URL)

draw_points(point)

screen.exitonclick()