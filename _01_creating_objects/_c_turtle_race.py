"""
Turtle Race
"""
import turtle
import random
import time
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()

    # TODO 1) Create an empty list of turtles

    t = 0
    turtles = list()
    for i in range(8):
        turtles.append(turtle.Turtle())
    for i in turtles:
    # TODO 2) Create a new turtle and set its shape to 'turtle
        i.shape('turtle')
    # TODO 3) Set the turtle's speed to 3
        i.speed(3)
    # TODO 4) Set the turtle's pen up
        i.penup()
    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen
        i.goto(-370, 190-(t*55))
        if t == 0:
            i.color('RED')
        elif t == 1:
            i.color('BLUE')
        if t == 2:
            i.color('GREEN')
        if t == 3:
            i.color('YELLOW')
        if t == 4:
            i.color('PURPLE')
        if t == 5:
            i.color('ORANGE')
        if t == 6:
            i.color('BROWN')
        if t == 7:
            i.color('PINK')
        t += 1
    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 7) Move each turtle forward a random distance between 1 and 20
    j = 1
    finished = False
    while not finished:
        for i in turtles:
            i.forward(random.randint(1, 20))
    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location
            if i.xcor() > 370:
                finished = True
                i.speed(5)
                for j in range(2):
                    i.left(45)
                    time.sleep(.5)
                    i.right(90)
                    time.sleep(.5)
                    i.left(90)
                    time.sleep(.5)
                    i.right(90)
                    time.sleep(.5)
                    i.left(405)
                i.goto(0, 0)
                i.turtlesize(20)
                i.right(1080)
                time.sleep(.15)
                i.turtlesize(1)
                i.shape('turtle')
                i.pensize(10)
                i.pencolor('CYAN')
                i.pendown()
                time.sleep(.5)
                i.speed(10)
                i.forward(5000)
                i.goto(-500, 0)
                i.forward(500)
                break
    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

    turtle.done()
