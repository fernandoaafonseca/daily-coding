from turtle import Turtle, Screen
import random
import time


STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
FONT = ('Arial', 22, 'bold')


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.speed = 10

    def create_snake(self):
        for pos in STARTING_POS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(pos)
            self.snake.append(new_segment)
    
    def increase_size(self):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.snake[-1].position())
        self.snake.append(new_segment)

    def increase_speed(self):
        self.speed += 5

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.forward(self.speed)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed('fastest')
        self.color('blue')
        self.create_food()

    def create_food(self):
        rand_x = random.randint(-290, 240)
        rand_y = random.randint(-290, 240)
        self.goto(rand_x, rand_y)
        

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.speed('fastest')
        self.goto(0, 250)
        self.draw_score_wall()
        self.update()
    
    def draw_score_wall(self):
        score_wall = Turtle()
        score_wall.penup()
        score_wall.color('grey')
        score_wall.speed('fastest')
        score_wall.shape('square')
        score_wall.pensize(100)
        score_wall.goto(-300, 300)
        score_wall.pendown()
        score_wall.goto(300, 300)

    def update(self):
        self.clear()
        self.write(f'Score: {self.points}', align='center', font=FONT)

    def increase_points(self):
        self.points += 1
        self.update()
        if self.points % 10 == 0:
            snake.increase_speed()
 
    def final_score(self):
        self.clear()
        self.goto(0, 25)
        self.color('red')
        self.write('GAME OVER!', align='center', font=FONT)
        self.goto(0, -25)
        self.write(f'Your final score is: {self.points}', align='center', font=FONT)


def create_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('-=-=-=-=-=- SNAKE -=-=-=-=-=-')
    screen.tracer(0)
    return screen


def keyboard():
    screen.listen()
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.up, 'w')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.down, 's')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.left, 'a')
    screen.onkeypress(snake.right, 'Right')
    screen.onkeypress(snake.right, 'd')


def game_engine():
    game_over = False
    while not game_over:
        screen.update()
        time.sleep(0.05)
        snake.move()

        if snake.head.distance(food) < 17:
            food.create_food()
            snake.increase_size()
            scoreboard.increase_points()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 245 or snake.head.ycor() < -290:
            game_over = True
            scoreboard.final_score()

        for segment in snake.snake[1:-1]:
            if snake.head.distance(segment) < 5:
                game_over = True
                scoreboard.final_score()


screen = create_screen()
snake = Snake()
kb = keyboard()
food = Food()
scoreboard = Scoreboard()
game_engine = game_engine()
screen.mainloop()