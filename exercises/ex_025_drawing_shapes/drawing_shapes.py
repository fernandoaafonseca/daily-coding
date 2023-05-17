from turtle import Turtle, Screen
from time import sleep
import random


def change_color(obj):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    obj.color(r, g, b)


def draw_dashed_line(obj):
    obj.penup()
    obj.goto(-450, -250)
    obj.pendown()
    obj.shape('classic')

    for _ in range(10):
        obj.pendown()
        obj.forward(10)
        obj.penup()
        obj.forward(10)


def draw_polygons(obj, start=3, end=11):
    obj.penup()
    obj.goto(-50, 400)
    obj.pendown()
    obj.shape('triangle')
    obj.speed('fastest')

    for i in range(start, end):
        change_color(obj)  
        for _ in range(i):
            obj.forward(100)
            obj.right(360/i)


def draw_circles(obj, times=72):
    obj.penup()
    obj.goto(-300, 200)
    obj.pendown()
    obj.shape('circle')
    obj.speed('fastest')
    
    for _ in range(times):
        change_color(obj)
        obj.circle(50)
        obj.right(5)


def random_walk(obj):
    obj.penup()
    obj.goto(0, 0)
    obj.pendown()
    obj.shape('turtle')
    obj.color('purple')
    obj.speed('fast')
    obj.pensize(10)

    degrees = [0, 90, 180, 270]
    turns = random.randint(10, 1000)

    for _ in range(turns):
        change_color(obj)
        direction = random.choice(degrees)
        obj.setheading(direction)
        obj.forward(25)


screen = Screen()
screen.colormode(255)
point = Turtle()

draw_dashed_line(point)

draw_polygons(point)

draw_circles(point)

random_walk(point)

screen.exitonclick()