from turtle import *

def draw_fish():
    speed(13) 
    bgcolor("Light blue") 
    pensize(10) 
    penup()
    goto(100, 0)
    pendown()
    goto(20, 50)
    goto(20, -50)
    goto(100, 0)
    seth(60)
    circle(-120, 120)
    seth(-120)
    circle(-120, 120)
    penup()
    fillcolor("#FF1493")
    pensize(7)
    goto(250, 5)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    penup()
    fillcolor("#3366cc")
    pensize(1)
    goto(250, 70)
    pendown()
    begin_fill()
    circle(-15)
    for i in range(4):
        penup()
        seth(150)
        fd(55+10*i)
        pendown()
        circle(-20-5*i)
    end_fill()
    done()

def draw_circle():
    speed(15)
    bgcolor("Light green")
    pensize(10)
    penup()
    goto(0,-200)
    pendown()
    for i in range(12):
        circle(200,30)
        circle(20)
        fillcolor("#E6E6FA")
        pensize(7)
        begin_fill()
        circle(30)
        end_fill()
    done()

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for fish, 2 for circle)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_fish()
        elif a == 2:
            draw_circle()
        else:
            print("Please input the value in [1,2]")
    except:
        print("Please input the value in [1,2]")
