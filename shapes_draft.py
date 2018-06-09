import turtle


def draw_shape():

    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)

    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    w = turtle.Turtle()
    w.shape("circle")
    w.color("red")
    w.rt(180)
    w.fd(100)
    w.lt(90)
    w.fd(100)
    w.lt(135)
    w.fd(100*(2 ** .5))

    window.exitonclick()

draw_shape()
