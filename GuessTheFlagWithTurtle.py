import random
import turtle

Turtle = turtle.Turtle()

def estonia():

    Turtle.fillcolor("blue")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(0, -30)
    Turtle.pd()

    Turtle.fillcolor("black")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(0, -60)
    Turtle.pd()

    Turtle.fillcolor("white")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()
    Turtle.hideturtle()

#estonia()

Turtle.goto(0,0)

def germany():

    Turtle.fillcolor("black")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(0, -30)
    Turtle.pd()

    Turtle.fillcolor("red")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(0, -60)
    Turtle.pd()

    Turtle.fillcolor("yellow")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(150)
        Turtle.rt(90)
        Turtle.fd(30)
        Turtle.rt(90)
    Turtle.end_fill()
    Turtle.hideturtle()

#germany()

Turtle.goto(0,0)

def italy():

    Turtle.fillcolor("green")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(50)
        Turtle.rt(90)
        Turtle.fd(90)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(50, 0)
    Turtle.pd()

    Turtle.fillcolor("white")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(50)
        Turtle.rt(90)
        Turtle.fd(90)
        Turtle.rt(90)
    Turtle.end_fill()

    Turtle.pu()
    Turtle.goto(100, 0)
    Turtle.pd()

    Turtle.fillcolor("red")
    Turtle.begin_fill()
    for i in range(2):
        Turtle.fd(50)
        Turtle.rt(90)
        Turtle.fd(90)
        Turtle.rt(90)
    Turtle.end_fill()

#italy()

flags = [italy, germany, estonia]

lives = 3
points = 0

while lives > 0 and len(flags) > 0:
    Turtle.reset()
    flagchoice = random.choice(flags)
    flagchoice()
    answer = input("Poia einai i simaia?")

    flags.remove(flagchoice)

    if answer == flagchoice.__name__:
        print("Bravo!")
        points = points + 1
        print("your points:", points)
        print("Your lives:", lives)

    else:
        print("Wrong answer!")
        points = points - 1
        lives = lives - 1
        print("Your points:", points)
        print("Your lives:", lives)

if lives == 0:
    print("You lost! Better luck next time!")
    turtle.bye()



turtle.done()