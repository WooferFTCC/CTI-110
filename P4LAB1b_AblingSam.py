# Samuel Abling
# P4LAB1b
# 03/19/2025
# Draws initials using turtles

# Import Library
import turtle


# Setup S drawing turtle
Bob = turtle

Bob.speed(0)
Bob.width(10)
Bob.hideturtle()

# Bob starts the S
Bob.rt(90)
for x in range(30):
    Bob.fd(1)
    Bob.lt(3)

# Setup James
James = Bob.clone()
James.speed(2)
James.hideturtle()

# Bob finishes the S
for x in range(60):
    Bob.fd(1)
    Bob.lt(3)
for x in range(90):
    Bob.fd(1)
    Bob.rt(3)

# James starts the A
James.up()
James.fd(50)
James.down()
James.lt(75)
James.fd(35)

# Setup Matt
Matt = James.clone()
Matt.hideturtle()

# James finishes
James.fd(45)
James.rt(150)
James.fd(80)

# Matt completes the A
Matt.rt(75)
Matt.fd(20)

# Celebrate
while True:
    Bob.lt(1)
    James.lt(1)
    Matt.lt(1)