from turtle import Turtle, Screen
import random


def create_screen():
    screen = Screen()
    screen.setup(width=600, height=400)
    screen.title('-=-=- Turtle Race -=-=-')
    screen.bgcolor('grey')
    return screen


def draw_finish_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.speed('slow')
    line.goto(280, -200)
    line.pendown()
    line.pensize(5)
    line.left(90)
    line.forward(400)
    line.hideturtle()

    dotted_line = Turtle()
    dotted_line.hideturtle()
    dotted_line.speed('fastest')
    dotted_line.penup()
    dotted_line.goto(275, -200)
    dotted_line.pendown()
    dotted_line.pensize(5)
    dotted_line.left(90)
    for _ in range(20):
        dotted_line.pendown()
        dotted_line.forward(20)
        dotted_line.penup()
        dotted_line.forward(20)

    dotted_line = Turtle()
    dotted_line.hideturtle()
    dotted_line.speed('fastest')
    dotted_line.penup()
    dotted_line.goto(270, -200)
    dotted_line.pendown()
    dotted_line.pensize(5)
    dotted_line.left(90)
    for _ in range(20):
        dotted_line.penup()
        dotted_line.forward(20)
        dotted_line.pendown()
        dotted_line.forward(20)

    dotted_line = Turtle()
    dotted_line.hideturtle()
    dotted_line.penup()
    dotted_line.speed('fastest')
    dotted_line.goto(265, -200)
    dotted_line.pendown()
    dotted_line.pensize(5)
    dotted_line.left(90)
    for _ in range(20):
        dotted_line.pendown()
        dotted_line.forward(20)
        dotted_line.penup()
        dotted_line.forward(20)

    line = Turtle()
    line.hideturtle()
    line.penup()
    line.speed('slow')
    line.goto(260, -200)
    line.pendown()
    line.pensize(5)
    line.left(90)
    line.forward(400)
    line.hideturtle()


def create_turtles():
    colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y_pos = [-90, -60, -30, 0, 30, 60, 90]
    turtles = []

    for color in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(-250, y_pos[colors.index(color)])
        new_turtle.speed('fastest')
        turtles.append(new_turtle)

    return turtles


def get_user_bet():
    user_bet = ''
    valid_bets = [1, 2, 3, 4, 5, 6, 7]
    while user_bet not in valid_bets:
        user_bet = ''
        while type(user_bet) != int:
            try:
                user_bet = int(user_bet)
                break
            except:
                user_bet = screen.textinput(title='Make your bet!', prompt='Who you think will win the race?\n\n\
    1 - black\n\
    2 - red\n\
    3 - orange\n\
    4 - yellow\n\
    5 - green\n\
    6 - blue\n\
    7 - purple\n')

    match user_bet:
        case 1:
            user_bet = 'black'
        case 2:
            user_bet = 'red'
        case 3:
            user_bet = 'orange'
        case 4:
            user_bet = 'yellow'
        case 5:
            user_bet = 'green'
        case 6:
            user_bet = 'blue'
        case 7:
            user_bet = 'purple'
    return user_bet


def race():
    game_over = False
    while not game_over:
        winner = ''
        for turtle in turtles:
            rand_speed = random.randint(0, 10)
            turtle.forward(rand_speed)
            if turtle.xcor() >= 241:
                color = turtle.color()
                winner = color[0]
                game_over = True
                return winner


def final_screen():
    final_text = Turtle()
    final_text.hideturtle()
    final_text.penup()
    final_text.goto(0, 150)
    final_text.write(f'The winner is {winner}!', align='center', font=('Arial', 20, 'normal'))
    final_text.goto(0, 100)

    if user_bet == winner:
        final_text.write(f'You got it right!', align='center', font=('Arial', 20, 'normal'))
    else:
        final_text.write(f'You lost the bet!', align='center', font=('Arial', 20, 'normal'))


screen = create_screen()
user_bet = get_user_bet()
draw_finish_line()
turtles = create_turtles()
winner = race()
final_screen()

screen.mainloop()