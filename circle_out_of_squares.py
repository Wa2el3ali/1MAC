import turtle


def circle():
 
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(20)

    for a in range(0, 360, 5):
        brad.rt(5)
        i = 0
        while i < 4:
            brad.forward(200)
            brad.right(90)
            i += 1

    window.exitonclick()

circle()
