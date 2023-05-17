from turtle import Turtle, Screen
import pandas as pd


MAP_IMAGE = 'imgs/blank_map.gif'
MAP_WIDTH = 725
MAP_HEIGHT = 491
CSV_FILE = 'data/states_coordinates.csv'
BIG_FONT = ('Courier', 28, 'bold')
SMALL_FONT = ('Courier', 10, 'normal')


def create_screen():
    screen = Screen()
    screen.title("USA states game")
    screen.setup(MAP_WIDTH, MAP_HEIGHT)
    screen.addshape(MAP_IMAGE)
    return screen


def draw_map():
    canvas = Turtle()
    canvas.shape(MAP_IMAGE)
    return canvas


def final_screen():
    missing_states = [state for state in states if state not in guessed_states]

    screen.setup(width=1000, height=1000)
    screen.clear()
    screen.bgcolor('purple')
    pointer = Turtle()
    pointer.penup()
    pointer.hideturtle()
    pointer.color('yellow')

    if len(guessed_states) == 50:
        pointer.goto(0, 50)
        pointer.write(f'CONGRATULATIONS!', font=BIG_FONT, align='center')
        pointer.goto(0, -50)
        pointer.write(f'You know all the USA States!', font=BIG_FONT, align='center')

    else:
        pointer.goto(-200, 50)
        pointer.write(f'GAME OVER!', font=BIG_FONT, align='center')

        pointer.goto(-200, -50)
        pointer.write(f'You guessed {len(guessed_states)}/50 States', font=BIG_FONT, align='center')

        pointer.color('white')
        pointer.goto(250, 400)
        pointer.write(f'Missing States:',font=BIG_FONT,  align='center')

        pointer.goto(250, 350)
        for missing_state in missing_states:
            new_y = pointer.ycor() - 15
            pointer.goto(pointer.xcor(), new_y)
            pointer.write(f'{missing_state}',font=SMALL_FONT,  align='center')

    screen.exitonclick()


def game_engine():
    game_over = False
    while not game_over:
        answer = ''
        if answer.lower() == 'exit' or len(guessed_states) == 50:
            final_screen()
            game_over = True
            break
        
        user_input = screen.textinput(title='Guess the State', prompt=f'Right answers: {len(guessed_states)}/50\n\nGuess a State name:')
        
        if user_input == None:
            final_screen()
            game_over = True
            break
        
        answer = user_input.strip().title()

        if answer in states and answer not in guessed_states:
            pointer = Turtle()
            pointer.speed('slowest')
            pointer.penup()
            state_data = df[df['state'] == answer]
            x_axis = int(state_data['x'])
            y_axis = int(state_data['y'])
            pointer.penup()
            pointer.goto(x_axis, y_axis)
            pointer.hideturtle()
            pointer.write(answer, font=SMALL_FONT)
            guessed_states.append(answer)
        

df = pd.read_csv(CSV_FILE)
states = df['state'].to_list()
guessed_states = []
screen = create_screen()
canvas = draw_map()
game_engine = game_engine()


screen.mainloop()