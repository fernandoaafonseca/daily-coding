import random
import time
from turtle import Turtle, Screen


FONT = ("Courier", 24, "normal")
PLAYER_STARTING_POSITION = (0, -280)
PLAYER_SPEED = 10
FINISH_LINE_Y = 280
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_SPEED = 5


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset_position()
        self.lives = 3

    def move(self):
        new_y = self.ycor() + PLAYER_SPEED
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(PLAYER_STARTING_POSITION)
  
    def decrease_lives(self):
        self.lives -= 1


class CarManager():

    def __init__(self):
        self.cars_list = []
        self.level_speed = 0

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars_list.append(new_car)

    def move_cars(self):
        random_speed = random.randint(1, 5)
        speed = CAR_STARTING_SPEED + random_speed + self.level_speed
        for car in self.cars_list:
            car.forward(speed)

    def increase_speed(self):
        self.level_speed += 3


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.update()

    def increase_level(self):
        self.current_level += 1

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f'Level: {self.current_level}', font=(FONT), align='left')
        self.goto(250, 250)
        self.write(f'Lives: {player.lives}', font=(FONT), align='right')

    def final_screen(self):
        screen.clear()
        screen.bgcolor('blue')
        self.color('white')
        self.goto(0, 50)
        self.write(f'GAME OVER!', font=(FONT), align='center')
        self.goto(0, -50)
        self.write(f'Your final level: {self.current_level}', font=(FONT), align='center')
        screen.exitonclick()


def create_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('grey')
    screen.title('Turtle crossing')
    screen.tracer(0)
    return screen


def keyboard():
    screen.listen()
    screen.onkeypress(player.move, 'Up')


def game_engine():
    game_over = False
    while not game_over:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        if player.ycor() >= FINISH_LINE_Y:
            player.reset_position()
            scoreboard.increase_level()
            scoreboard.update()
            car_manager.increase_speed()
        
        for car in car_manager.cars_list:
            if car.distance(player) < 25:
                player.decrease_lives()
                player.reset_position()
                scoreboard.update()
                if player.lives == 0:
                    game_over = True
                    scoreboard.final_screen()


screen = create_screen()
player = Player()
scoreboard = Scoreboard()
car_manager  = CarManager()
kb = keyboard()
engine = game_engine()
screen.mainloop()