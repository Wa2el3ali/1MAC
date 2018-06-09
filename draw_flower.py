import turtle


def flower():

    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(20)

    for a in range(0, 360, 5):
        brad.lt(5)
        i = 0
        while i < 2:
            brad.fd(100)
            brad.lt(30)
            brad.forward(100)
            brad.lt(150)
            i += 1
    brad.rt(90)
    brad.fd(300)

    window.exitonclick()

flower()
