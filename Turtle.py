from turtle import *
from random import *
speed(0)
penup()
goto(-140,140)
for step in range(15):
    write(step, align= "center")
    right(90)
    for num in range(8):
        
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
    
ashim = Turtle()
ashim.color("red")
ashim.shape("turtle")

ashim.penup()
ashim.goto(-160,120)
ashim.pendown()

for turn in range(10):
    ashim.right(36)


nonu = Turtle()
nonu.shape("turtle")
nonu.color("orange")

nonu.penup()
nonu.goto(-160,90)
nonu.pendown()

for turn in range(72):
    nonu.left(5)

nalla = Turtle()


nalla.color("blue")
nalla.shape("turtle")

nalla.penup()
nalla.goto(-160,60)
nalla.pendown()

for turn in range(10):
    nalla.right(36)
    


motu = Turtle()

motu.color("green")
motu.shape("turtle")

motu.penup()
motu.goto(-160,30)
motu.pendown()

for turn in range(72):
    motu.left(5)

jagga = Turtle()

jagga.color("violet")
jagga.shape("turtle")

jagga.penup()
jagga.goto(-160,0)
jagga.pendown()

for turn in range(10):
    jagga.right(36)
for turn in range(100):
    ashim.forward(randint(1,5))
    nonu.forward(randint(1,5))
    nalla.forward(randint(1,5))
    motu.forward(randint(1,5))
    jagga.forward(randint(1,5))
    
