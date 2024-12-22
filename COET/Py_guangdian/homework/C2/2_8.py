import turtle

pen = turtle.Turtle()

pen.speed(100)
pen.color("pink")

def draw_line(a):
    pen.forward(a)
    pen.right(90)

while True:
    for i in range(200):
       draw_line(2*i)
    turtle.done()