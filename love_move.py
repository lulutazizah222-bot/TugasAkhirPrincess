import turtle
import math
import time

#setup layar
turtle.bgcolor("black")
turtle.title("Love Animation in Python ❤️")
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)

#fungsi koordinat hati 
def hearta(k):
    return 16 *math.sin(k) ** 3

def heartb(k):
    return 13 *math.cos(k) - 5 *math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

#fungsi gambar hati dengan ukuran tertentu
def draw_heart(scale, color):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    for k in range(0, 360):
        x = hearta(math.radians(k)) *scale
        y = heartb(math.radians(k)) *scale
        turtle.goto(x, y)

        turtle.end_fill()

# Animasi hati berdenyut
colors = ["red", "deppink", "hotpink", "pink"]
while True:
   for scale in [15, 16, 17, 18, 17, 16,]: # efek denyut
       turtle.clear()
       draw_heart(scale, colors[scale % len(colors)])
       time.sleep(0.1)