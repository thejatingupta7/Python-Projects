from turtle import *
import random
'''
import colorgram
colors = colorgram.extract("Project_18_Hirst_spot.jpeg", 72)
print(colors)           # it contains both rgb and hsl colors

# for separating rgb colors we make a loop
rgb = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)
print(rgb)
'''


# now take the rgb list from console and get a list
colormode(255)
rgb_list = [(253, 246, 251), (241, 253, 246), (243, 247, 253), (240, 231, 56), (221, 154, 74), (185, 64, 30), (239, 42, 120), (191, 12, 32), (35, 96, 173), (45, 213, 79), (20, 24, 54), (37, 35, 156), (234, 228, 4), (87, 185, 220), (220, 163, 10), (205, 12, 6), (196, 37, 78), (49, 25, 15), (74, 12, 47), (233, 58, 37), (26, 144, 31), (84, 236, 176), (80, 211, 144), (219, 138, 183), (12, 200, 218), (95, 75, 12), (241, 157, 197), (75, 80, 217), (11, 36, 28), (17, 92, 61), (239, 171, 160), (108, 223, 234), (176, 180, 228), (251, 7, 22), (253, 9, 4), (78, 42, 225), (8, 246, 222)]
t = Turtle()
t.speed(20)
t.hideturtle()              # hides the pen/turtle



def dot_line():
    for _ in range(10):
        dot_color = random.choice(rgb_list)
        t.pd()
        t.dot(20, dot_color)
        t.pu()
        t.fd(50)

t.pu()
t.setheading(225)
t.fd(300)
t.setheading(0)
dot_line()

for i in range(9):
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(500)
    t.left(180)
    dot_line()

done()

