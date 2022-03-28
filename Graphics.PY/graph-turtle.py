###
# Python turtle test example.
# 
# License - MIT.
###

import os
import time
from turtle import *



# draw_flower - flower.
def draw_flower():
# {
    color('red', 'yellow')

    begin_fill()

    while True:
        forward(200)
        left(170)

        if abs(pos()) < 1:
            break

    end_fill()
# }


# draw_star - Star.
def draw_star():
# {
    color('black', 'yellow')

    begin_fill()

    penup()
    goto(0, 0)
    pendown()

    # set heading is 0
    setheading(0)

    for i in range(5):
        forward(40)
        right(144)

    end_fill()
# }


# draw_trapezoid - Trapezoid.
def draw_trapezoid():
# {
    forward(180)
    left(120)

    forward(80)
    left(60)

    forward(100)
    left(60)

    forward(80)
# }


# draw_triangle - Triangle.
def draw_triangle():
# {
    begin_fill()

    forward(100)
    left(120)

    forward(100)
    left(120)

    forward(100)

    end_fill()
# }


# draw_rectangle - Rectangle.
def draw_rectangle():
# {
    forward(100)
    right(90)

    forward(100)
    right(90)

    forward(100)
    right(90)

    forward(100)
# }


# draw_circular - Circular.
def draw_circular():
# {
    circle(100)
# }


# background_color - Set background color.
def background_color():
# {
    colors_list = (
        'Red',
        'Orange',
        'Yellow',
        'Green',
        'Blue',
        'Black',
        'White'
    )

    corlen = len(colors_list)

    for i in range(corlen):
        bgcolor(colors_list[i])

        time.sleep(1)
# }


# clear_screen - Clear screen.
def clear_screen():
# {
    time.sleep(1)

    clearscreen()
# }


# Main function.
def main():
# {
    # Example 1: set background color.
    background_color()

    # Example 2: draw circular.
    draw_circular()
    clear_screen()

    # Example 3: draw rectangle.
    draw_rectangle()
    clear_screen()

    # Example 4: draw triangle.
    draw_triangle()
    clear_screen()

    # Example 5: draw trapezoid.
    draw_trapezoid()
    clear_screen()

    # Example 6: draw star.
    draw_star()
    clear_screen()

    # Example 7: draw flower.
    draw_flower()

    done()
# }


# Program entry.
if '__main__' == __name__:
    main()
