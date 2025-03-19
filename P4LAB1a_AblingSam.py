# Samuel Abling
# P4LAB1a
# 03/19/2025
# Draws a square and triangle (plus a little extra) using the py turtle.

# Import library
import turtle
 
# Set inital turtle speed
turtle.speed(2)

# Position for the square
turtle.up()
turtle.bk(50)
turtle.down()

# Draw square
for x in range(4):
    turtle.fd(100)
    turtle.lt(90)


# Position for the triangle
turtle.up()
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(25)
turtle.rt(180)
turtle.down()


# Draw triangle
for x in range(3):
    turtle.fd(150)
    turtle.lt(120)


# Position for a rectangle
turtle.up()
turtle.fd(50)
turtle.rt(90)
turtle.fd(100)
turtle.down()

# Draw rectangle
turtle.bk(50)
turtle.lt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(50)

# Position for a circle
turtle.up()
turtle.lt(90)
turtle.fd(45)
turtle.lt(90)
turtle.fd(45)
turtle.down()

turtle.speed(0)

# Draw circle
for x in range(90):
    turtle.fd(1)
    turtle.lt(4)

# Goto rectangle
turtle.up()
turtle.bk(40)
turtle.lt(90)
turtle.fd(55)

# Turtle enjoys its new home
while True:
    turtle.lt(10)