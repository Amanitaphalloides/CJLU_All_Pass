import turtle

turtle.color("black", "red")
turtle.begin_fill()
for i in range(5):
    turtle.seth(i*216)
    turtle.fd(200)
turtle.end_fill()
turtle.done()