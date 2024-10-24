import random
import turtle


'''
Constants for screen and drawing configuration.
'''
# Those values creates a square window on default 16:9 screens
# Turtle screen width of 50% of the screen size
SCREEN_WIDTH = 0.5
# Turtle screen height of 90% of the screen size
SCREEN_HEIGHT = 0.9
SCREEN_TITLE = 'Psychedelic Square Spiral'
DRAWING_SPEED = 0
# Total number of lines to draw
NUM_OF_LINES = 600
# Thickness of the lines
LINE_SIZE = 2
# Angle for spiral effect
ANGLE = 89
# Angle for changing the drawing direction
ANGLE_DIRECTION = 90

# Start the RGB values for the background color with "black" (0, 0, 0)
rgb_bgcolor_value = 0
# Control variable for background color cycling
is_increasing = True
# Control how fast the background color cycles
CYCLE_SPEED = 6


def main():
    '''
    Main function to initialize the turtle and execute the drawing.
    '''
    t = init_turtle(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,
                    rgb_bgcolor_value, LINE_SIZE, DRAWING_SPEED)
    # Draw the first spiral
    draw_forward_squares(t, NUM_OF_LINES, ANGLE)
    # Change direction after first spiral
    change_drawing_direction(t, ANGLE_DIRECTION)
    # Draw the second spiral backwards
    draw_backward_squares(t, NUM_OF_LINES, ANGLE)
    # Wait for click to close window
    t.screen.exitonclick()


def init_turtle(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, BG_COLOR, LINE_SIZE, DRAWING_SPEED):
    '''
    Initialize the Turtle module with given parameters and settings.
    '''
    t = turtle.Turtle()
    t.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    t.screen.title(SCREEN_TITLE)
    t.screen.bgcolor(rgb_bgcolor_value, rgb_bgcolor_value, rgb_bgcolor_value)
    t.pensize(LINE_SIZE)
    t.speed(DRAWING_SPEED)

    # Set the color mode to RGB (r, g, b) values
    turtle.colormode(255)
    # Hide the Turtle arrow icon
    t.hideturtle()
    return t


def get_random_color():
    '''
    Return the values for a random RGB color.

    Returns:
    tuple: Random RGB color values as integers.
    '''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def change_bgcolor(rgb_bgcolor_value=0, is_increasing=True):
    '''
    Change the background color value in a cycling manner, from black to gray, then from gray to black indefinitely.

    If the current value is less than 128, it increases; 
    if it reaches 128, it switches to decreasing until it hits 0, 
    then it starts is_increasing again.

    Parameters:
    rgb_bgcolor_value (int): The current RGB background color value.
    is_increasing (bool): Indicates whether to increase or decrease the value.

    Returns:
    tuple: Updated RGB background color value and direction.
    '''
    global CYCLE_SPEED

    if is_increasing:
        # Increase the RGB color value until it reaches 128
        if rgb_bgcolor_value < 128:
            rgb_bgcolor_value += CYCLE_SPEED
        else:
            # Switch to decreasing when the value reaches 128
            rgb_bgcolor_value -= CYCLE_SPEED
            is_increasing = False
    else:
        # Decrease the RGB color value until it reaches 0
        if rgb_bgcolor_value > 0:
            rgb_bgcolor_value -= CYCLE_SPEED
        else:
            # Switch to is_increasing when the value reaches 0
            rgb_bgcolor_value += CYCLE_SPEED
            is_increasing = True

    # Return updated value and direction
    return rgb_bgcolor_value, is_increasing


def draw_forward_squares(t, NUM_OF_LINES, ANGLE):
    '''
    Draw squares moving forward, creating a spiral effect.

    Parameters:
    t (turtle.Turtle): The turtle instance used for drawing.
    NUM_OF_LINES (int): Total number of lines to draw.
    ANGLE (int): Angle to turn for the spiral effect.
    '''
    global rgb_bgcolor_value
    global is_increasing

    for i in range(NUM_OF_LINES):
        r, g, b = get_random_color()
        # Set random pen color
        t.pencolor(r, g, b)
        # Move forward with is_increasing length
        t.forward(i + 1)
        # Turn right by the given angle
        t.right(ANGLE)

        rgb_bgcolor_value, is_increasing = change_bgcolor(
            rgb_bgcolor_value, is_increasing)
        t.screen.bgcolor(rgb_bgcolor_value,
                         rgb_bgcolor_value, rgb_bgcolor_value)


def draw_backward_squares(t, NUM_OF_LINES, ANGLE):
    '''
    Draw squares moving backward, reversing the spiral effect.

    Parameters:
    t (turtle.Turtle): The turtle instance used for drawing.
    NUM_OF_LINES (int): Total number of lines to draw.
    ANGLE (int): Angle to turn for the spiral effect.
    '''
    global rgb_bgcolor_value
    global is_increasing

    # Reverse loop
    for i in range(NUM_OF_LINES, 0, -1):
        r, g, b = get_random_color()
        # Set random pen color
        t.pencolor(r, g, b)
        # Move forward with decreasing length
        t.forward(i + 1)
        # Turn left by the given angle
        t.left(ANGLE)

        rgb_bgcolor_value, is_increasing = change_bgcolor(
            rgb_bgcolor_value, is_increasing)
        t.screen.bgcolor(rgb_bgcolor_value,
                         rgb_bgcolor_value, rgb_bgcolor_value)


def change_drawing_direction(t, new_angle):
    '''
    Change the Turtle's drawing direction by rotating it.

    Parameters:
    t (turtle.Turtle): The turtle instance to change direction.
    new_angle (int): The angle to rotate the turtle.
    '''
    # Rotate the turtle by the given angle
    t.right(new_angle)


if __name__ == '__main__':
    main()
