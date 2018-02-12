import turtle

def draw_something():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.color('orange')
    brad.shape('turtle')
    brad.hideturtle()
    brad.speed(0)



    for j in range(50):
        j = j * 10
        for i in range(4):
            brad._rotate(j)
            brad.forward(100)
            brad.right(90+j)

    brad.pensize(3)
    brad.right(90)
    brad.forward(500)

    window.exitonclick()
draw_something()
