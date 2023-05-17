from turtle import Turtle, Screen


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def exit_screen():
    screen.bye()

turtle = Turtle()
screen = Screen()
screen.listen()

screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(clear_screen, 'space')
screen.onkeypress(exit_screen, 'Escape')

screen.mainloop()