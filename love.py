heart = [
"  *****     *****  ",
" *******   ******* ",
"********* *********",
"*******************",
 " ***************** ",
 "  ***************  ",
 "   *************   ",
 "    ***********    ",
 "     *********     ",
 "      *******      ",
 "       *****       ",
 "        ***        ",
 "         *         ",
]

message = "I LOVE YOU"

for i, line in enumerate(heart):
    # center message in the middle row (approx)
    if i == len(heart)//2:
        # place message in center of width
        width = len(heart[0])
        msg = message.center(width)
        print(msg)
    else:
        print(line)

# turtle_heart.py
import turtle
import math

screen = turtle.Screen()
screen.title("Heart with Turtle ❤️")
screen.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("red")
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()

# parametric heart: x = 16 sin^3 t, y = 13 cos t - 5 cos 2t - 2 cos 3t - cos 4t
# scale to fit screen
scale = 10
first = True
for deg in range(0, 360*2, 2):  # trace curve twice for smoothness
    t_rad = math.radians(deg/2)  # reduce frequency for nicer shape
    x = 16 * math.sin(t_rad)**3
    y = 13 * math.cos(t_rad) - 5 * math.cos(2*t_rad) - 2 * math.cos(3*t_rad) - math.cos(4*t_rad)
    x *= scale
    y *= scale
    if first:
        t.penup()
        t.goto(x, y-50)  # shift down a bit
        t.pendown()
        first = False
    else:
        t.goto(x, y-50)
t.end_fill()

# Write message
t.penup()
t.goto(0, -10)
t.color("white")
t.write("I ♥ YOU", align="center", font=("Arial", 24, "bold"))

turtle.done()