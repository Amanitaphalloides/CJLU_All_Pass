import turtle

pen = turtle.Turtle()

pen.speed(10)
pen.color("pink")

def draw_tri():
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    pen.forward(100)
    pen.right(60)

while True:
    pen.right(30)
    for _ in range(6):
       draw_tri()
    turtle.done()