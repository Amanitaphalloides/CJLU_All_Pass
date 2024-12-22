import turtle

import random

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
#    turtle.pencolor((int(random.random()*255),int(random.random()*255),int(random.random()*255)))
    turtle.pencolor((random.random(), random.random(), random.random()))
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)

turtle.done()