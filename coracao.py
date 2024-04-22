import turtle


screen = turtle.Screen()
screen.bgcolor("white")


my_turtle = turtle.Turtle()


my_turtle.pencolor("red")
my_turtle.pensize(3)

my_turtle.begin_fill()
my_turtle.left(140)
my_turtle.forward(180)
my_turtle.circle(-90, 200)
my_turtle.setheading(60)
my_turtle.circle(-90, 200)
my_turtle.forward(180)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(0, -150)
my_turtle.pendown()
my_turtle.write("mag te amo", font=("lobster", 20, "normal"))

my_turtle.hideturtle()

turtle.done()
