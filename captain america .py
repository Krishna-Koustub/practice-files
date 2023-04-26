# Import module turtle

# Python module is built-in toolbox, toolbox here will be able to use the import

# turtle Python module is used to drawing toolbox

import turtle

 

# The turtle inside the tools out, is assigned to the variable t

# Zhaomaohuahu it wants, these things are going to back to understand

t = turtle.Turtle()

 

# This line is used to accelerate the speed of the brush, from 1 to 9, in turn faster, but 0 is the fastest

t.speed(0)

 

# This is a move forward in pixels

t.forward(100)

# This is turn, is a unit of angle

t.right(120)

t.forward(100)

t.right(120)

t.forward(100)

t.right(120)

# Copy three times, drew a triangle

 

# square

# rectangle

 

# If we need to change the side length of the triangle's how to do?

# This use to variables, and that time can be changed simply by changing the variable length

# If the same variable, defined later overwrite the previous

l = 200

t.forward(l)

t.right(120)

t.forward(l)

t.right(120)

t.forward(l)

t.right(120)

 

# for cycle

# There loop while loop, taking into account the need not not talk about it

# Loop processing for repeating things

 

# range() It is an interval

# range(3) Equivalent to 012

# range(5) Corresponding to 01,234

 

# i Take the range () in value, take a time, take once again cycle

# After the colon must be retracted, retracting the representative block is the same

# By shining on the line, attention can not be mistyped a character, you can not use Chinese symbols

for i in range(3):

   t.forward(l)

   t.right(120)

 

 

# If you want to draw two triangles how to do, and then copy a for loop?

# We use function code is encapsulated, that time called directly like

# def Keyword is used to define the function, triangle function name

# Colon must be connected indentation, which is also a function block

def triangle():

   for i in range(3):

       t.forward(l)

       t.right(120)

 

 

# Call functions

# triangle()

 

 

# Function parameters can be passed into

def triangle2(l):

   for i in range(3):

       t.forward(l)

       t.right(120)

 

 

# You need to pass parameters into account in order to call this function

# triangle2(250)

 

# Given a rectangular function Videos

 

# Arithmetic

#   +   plus

#   -   Less

#   *   Multiply

#   /   except

#   //  Divisible

#   %   Remainder

 

# Videos write a general function n-gon

def polygon(l, n):

   angle = 360 / n

   for i in range(n):

       t.forward(l)

       t.right(angle)

 

 

# polygon(100, 6)

 

 

# Draw a five-pointed star

def five_star(l):

   for i in range(5):

       t.forward(l)

       t.right(144)

 

 

# five_star(100)

 

 

# Draw a circle

# Side length of 36 or more is a circle

def circle():

   for i in range(36):

       t.forward(10)

       t.right(15)

 

 

# circle()

 

 

# Paint the specified coordinates

# For example, to draw a square in the coordinate (100, 150) a position

def square(x, y, l):

   t.penup()

   t.goto(x, y)

   t.pendown()

   for i in range(4):

       t.forward(l)

       t.right(90)

 

 

# square(100, 150, 100)

 

# As a function of the pen is positioned using the package, will be able to effectively remove duplicate code

def setpen(x, y):

   t.penup()

   t.goto(x, y)

   t.pendown()

   t.setheading(0)

 

 

def square(x, y, l):

   setpen(x, y)

   for i in range(4):

       t.forward(l)

       t.right(90)

 

 

# square(100, 150, 100)

 

 

# Painting a row of square, a total of five, spacing 10

# Stupid

# square(100, 150, 30)

# square(140, 150, 30)

# square(180, 150, 30)

# square(220, 150, 30)

# square(260, 150, 30)

 

 

# Using a for loop, function

 

def square_line(x, y, l, n, dis):

   for i in range(n):

       inner_x = x + (l + dis) * i

       square(inner_x, y, l)

 

 

# square_line(100, 150, 30, 6, 10)

 

 

# Draw a square matrix

def square_matrix(x, y, l, n, dis, m):

   for i in range(m):

       inner_y = y - (l + dis) * i

       square_line(x, inner_y, l, n, dis)

 

 

# square_matrix(100, 150, 30, 5, 10, 6)

 

 

# Fill color, to color graphics

def five_star(l):

   t.fillcolor('yello')

   t.begin_fill()

   for i in range(5):

       t.forward(l)

       t.right(144)

   t.end_fill()

 

# five_star(100)

 

# Simple usage dictionary

 

# Abstract paintings

# for i in range(500):

#     t.forward(i)

#     t.left(90)

 

# for i in range(500):

#     t.forward(i)

#     t.left(91)

 

colors = ['red', 'yellow', 'blue', 'green']

 

 

# for i in range(500):

#     t.pencolor(colors[i % 4])

#     t.circle(i)

#     t.left(91)

 

# sides = 5

# colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']

# for i in range(360):

#     t.pencolor(colors[i % sides])

#     t.forward(i * 3 / sides + i)

#     t.left(360 / sides + 1)

#     t.width(i * sides / 200)

 

# US team Shield

def circle(x, y, r, color):

   n = 36

   angle = 360 / n

   pi = 3.1415926

   c = 2 * pi * r

   l = c / n

   start_x = x - l / 2

   start_y = y + r

   setpen(start_x, start_y)

   t.pencolor(color)

   t.fillcolor(color)

   t.begin_fill()

   for i in range(n):

       t.forward(l)

       t.right(angle)

   t.end_fill()

 

 

def five_star(l):

   setpen(0, 0)

   t.setheading(162)

   t.forward(150)

   t.setheading(0)

   t.fillcolor('WhiteSmoke')

   t.begin_fill()

   t.hideturtle()

   t.penup()

   for i in range(5):

       t.forward(l)

       t.right(144)

   t.end_fill()

 

 

def sheild():

   circle(0, 0, 300, 'red')

   circle(0, 0, 250, 'white')

   circle(0, 0, 200, 'red')

   circle(0, 0, 150, 'blue')

   five_star(284)

 

 

sheild()

 

# End of the line must have, according with the line

turtle.done()

 

