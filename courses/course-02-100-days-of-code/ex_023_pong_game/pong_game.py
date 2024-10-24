from turtle import Turtle, Screen
import time
import random


FONT = ('Courier', 28, 'normal')


class Paddle(Turtle):

    def __init__(self, i):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed = 30
        self.create_player(i)


    def create_player(self, i):
        if i == 1:
            self.goto(-450, 0)
        elif i == 2:
            self.goto(450, 0)

    
    def move_up(self):
        if self.ycor() <= 200:
            new_y = self.ycor() + self.speed
            self.goto(self.xcor(), new_y)


    def move_down(self):
        if self.ycor() >= -200:
            new_y = self.ycor() - self.speed
            self.goto(self.xcor(), new_y)

    
    def get_mode(self):
        self.mode = ''
        self.valid_nums = [0, 1, 2, 3, 4, 5]
        while self.mode not in self.valid_nums:
            self.mode = ''
            while type(self.mode) != int:
                try:
                    self.mode = int(self.mode)
                    break
                except:
                    self.mode = screen.textinput(title='Game setting', prompt='Choose the mode:\n\n\
0 - 👥 2 players\n\
1 - 💻 very easy\n\
2 - 💻 easy\n\
3 - 💻 normal\n\
4 - 💻 hard\n\
5 - 💻 impossible\n')

        match self.mode:
            case 0:
                self.mode = 0
            case 1:
                self.mode = 99
            case 2:
                self.mode = 95
            case 3:
                self.mode = 89
            case 4:
                self.mode = 85
            case 5:
                self.mode = 2

        
    def ai_movement(self):
        self.offset = 10

        if ball.heading() < 90 or ball.heading() > 270:       
            choice = random.randint(1, 100) 
            if ball.ycor() > self.ycor() + self.offset:
                if self.mode <= choice:
                    self.move_up()
                else:
                    pass
            elif ball.ycor() < self.ycor() - self.offset:
                if self.mode <= choice:
                    self.move_down()
                else:
                    pass


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
    

    def create_ball(self):
        self.penup()
        self.goto(0, 0)
        self.color('white')
        self.shape('square')
        self.shapesize(1.25, 1.25)
        self.speed = 3
        direction = [-self.speed, self.speed]
        self.x_move = random.choice(direction)
        self.y_move = random.choice(direction)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    # def change_speed(self):
    #     self.speed *= 10
    #     return self.speed


    def change_x(self):
        self.x_move *= -1


    def change_y(self):
        self.y_move *= -1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_points = 0
        self.p2_points = 0
        self.penup()
        self.color('black')
        self.hideturtle()
        self.draw_score()

    
    def add_p1(self):
        self.p1_points += 1
        self.draw_score()

    
    def add_p2(self):
        self.p2_points += 1
        self.draw_score()


    def draw_score(self):
        self.clear()
        self.goto(25, 260)
        self.write(f'{self.p1_points}', align='center', font=FONT)
        self.goto(0, 260)
        self.write('x', align= 'center', font=FONT)
        self.goto(-25, 260)
        self.write(f'{self.p2_points}', align='center', font=FONT)
        time.sleep(0.5)


    def final_screen(self):
        screen.clear()
        self.clear()
        self.goto(0, 99)
        self.color('blue')
        self.write('GAME OVER!', align='center', font=FONT)
        self.goto(0, 33)
        self.write(f'Final score:', align='center', font=FONT)
        self.goto(0, -33)
        self.write(f'{self.p1_points} X {self.p2_points}', align='center', font=FONT)
        self.write(f'', align='center', font=FONT)
        screen.exitonclick()


class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('grey')
        self.speed('fastest')
        self.shape('square')
        self.net_size = 9
        self.borders()
        self.net()
        self.net_bands()

    def borders(self):
        self.pensize(70)
        self.goto(-500, 300)
        self.pendown()
        self.goto(500, 300)
        self.goto(500, -300)
        self.goto(-500, -300)
        self.goto(-500, 300)

    def net(self):
        self.counter = 2
        self.penup()
        self.goto(-10, -300)
        for i in range(-300, 300, self.net_size):
            self.pensize(5)
            if self.counter % 2 == 0:
                self.penup()
                self.goto(-10, i)
                self.counter += 1
            else:
                self.pendown()
                self.goto(-10, i)
                self.counter += 1

        self.counter = 2
        self.penup()
        self.goto(-5, -300)
        for i in range(-300, 300, self.net_size):
            self.pensize(5)
            if self.counter % 2 == 0:
                self.pendown()
                self.goto(-5, i)
                self.counter += 1
            else:
                self.penup()
                self.goto(-5, i)
                self.counter += 1

        self.counter = 2
        self.penup()
        self.goto(0, -300)
        for i in range(-300, 300, self.net_size):
            self.pensize(5)
            if self.counter % 2 == 0:
                self.penup()
                self.goto(0, i)
                self.counter += 1
            else:
                self.pendown()
                self.goto(0, i)
                self.counter += 1

        self.counter = 2
        self.penup()
        self.goto(5, -300)
        for i in range(-300, 300, self.net_size):
            self.pensize(5)
            if self.counter % 2 == 0:
                self.pendown()
                self.goto(5, i)
                self.counter += 1
            else:
                self.penup()
                self.goto(5, i)
                self.counter += 1

        self.counter = 2
        self.penup()
        self.goto(10, -300)
        for i in range(-300, 300, self.net_size):
            self.pensize(5)
            if self.counter % 2 == 0:
                self.penup()
                self.goto(10, i)
                self.counter += 1
            else:
                self.pendown()
                self.goto(10, i)
                self.counter += 1

    def net_bands(self):
        self.counter = 2
        self.color('grey')
        self.penup()
        self.goto(-14, -265)
        self.pensize(4)
        for i in range(-265, 265):
            self.pendown()
            self.goto(-14, i)
            self.counter += 1
        
        self.counter = 2
        self.penup()
        self.goto(14, -265)
        for i in range(-265, 265):
            self.pendown()
            self.goto(14, i)
            self.counter += 1
        self.hideturtle()


def create_screen():
    screen = Screen()
    screen.setup(width=1000, height=600)
    screen.bgcolor('black')
    screen.title('-=-=-=-=-=- PONG -=-=-=-=-=-')
    screen.tracer(0)
    return screen


def keyboard():
    screen.listen()
    screen.onkeypress(player_1.move_up, 'w')
    screen.onkeypress(player_1.move_down, 's')
    if player_2.mode == 0:
        screen.listen()
        screen.onkeypress(player_2.move_up, 'Up')
        screen.onkeypress(player_2.move_down, 'Down')


def game_engine():
    game_over = False
    while not game_over:
        time.sleep(0.001)
        ball.move()
        screen.update()
        
        if ball.ycor() > 250 or ball.ycor() < -250:
            ball.change_y()

        if ball.xcor() < -480:
            scoreboard.add_p1()
            ball.create_ball()
        elif ball.xcor() > 480:
            scoreboard.add_p2()
            ball.create_ball()

        if player_2.mode != 0:
            player_2.ai_movement()

        if ball.distance(player_1) < 40 and ball.xcor() < -450:
            ball.change_x()

        elif ball.distance(player_2) < 40 and ball.xcor() > 450:           
            ball.change_x()
           
        if scoreboard.p1_points == 10 or scoreboard.p2_points == 10:
            game_over = True
            scoreboard.final_screen()


screen = create_screen()
player_1 = Paddle(i=1)
player_2 = Paddle(i=2)
player_2.get_mode()
kb = keyboard()
table = Table()
ball = Ball()
scoreboard = Scoreboard()
game = game_engine()

screen.mainloop()