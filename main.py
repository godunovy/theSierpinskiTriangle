import random
import turtle

# main triangle dimensions
triangle_side = 700

draw = turtle.Turtle()
wn = turtle.Screen()

# window config
wn.setup(width=800, height=800)
wn.title("The Sierpinski Triangle")
turtle.bgcolor("black")
draw.speed(0)
draw.penup()

# main triangle positions
a = (-350, -350)
b = tuple
c = tuple

# draw main triangle and assign coordinates to b, c
draw.goto(a)
draw.dot(3, "green")
draw.left(60)
draw.forward(triangle_side)
draw.dot(3, "green")

b = draw.position()

draw.right(120)
draw.forward(triangle_side)

c = draw.position()

draw.dot(3, "green")
draw.left(60)

start = (0, 0)  # it can be anywhere on the triangle area
draw.goto(start)


run = True
while run:

    roll_dice = random.randint(1, 3)

    # randomly choose direction for next move
    to_A, to_B, to_C = False, False, False

    if roll_dice == 1:
        to_A = True

    elif roll_dice == 2:
        to_B = True

    else:
        to_C = True

    # draw dot according Chaos Theory
    def draw_dot(direction):

        angle = draw.towards(direction)
        draw.setheading(angle)
        half_way = draw.distance(direction) / 2
        draw.forward(half_way)
        draw.dot(3, "green")
        draw.setheading(0)


    if to_A:
        draw_dot(a)

    elif to_B:
        draw_dot(b)

    else:
        draw_dot(c)


wn.bye()
