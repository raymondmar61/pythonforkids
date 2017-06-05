#use turtle module
#use python shell.  Type "python3.5".  Next type "import turtle".
import turtle

t=turtle.Pen()
#draw a square
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.reset() #erase canvas, turtle returns to starting position
t.clear() #erase canvas, turtle remains in position

#use for loop to draw a square
import turtle
t=turtle.Pen()
t.reset()
for x in range(1,5):
	t.forward(50)
	t.left(90)

import turtle
t=turtle.Pen()
#draw two parallel lines
t.reset()
t.backward(100)
t.up() #pick up the pen and stop drawing
t.right(90)
t.forward(20)
t.left(90)
t.down() #put down the pen and start drawing
t.forward(100)

#draw a star
import turtle
t=turtle.Pen()
t.reset()
for x in range(1,9):
	t.forward(100)
	t.left(225)

#draw a star
import turtle
t=turtle.Pen()
t.reset()
for x in range(1,38):
	t.forward(100)
	t.left(175)

#draw a star
import turtle
t=turtle.Pen()
t.reset()
for x in range(1,20):
	t.forward(100)
	t.left(95)

#we can create a variety of shapes using for loops.  Without for loops, our code would have required a lot of tedious typing
#let's use an if statement to control how the turtle turns and draws.  We want the turtle to turn one angle the first time and another angle the next time
import turtle
t = turtle.Pen()
t.reset()
for x in range(1, 19):
	t.forward(100)
	if x % 2 == 0:
		t.left(175)
	else:
		t.left(225)

#drawing a car
import turtle
t = turtle.Pen()
t.reset()
t.color(1,0,0) #color changes the color of the pen using RGB (r,g,b) from 0 to 1 as a percentage
t.begin_fill() #fill in an area of the canvas with a color
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill() #stops fill in an area of the canvas with a color
#first wheel
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10) #draws a circle of a particular size
t.end_fill()
#second wheel
t.setheading(0) #turns the turtle to face a particular direction
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

#a square drawing function
import turtle
t = turtle.Pen()
t.reset()
def mysquare(size):
	t = turtle.Pen()
	for x in range(1,5):
		t.forward(size)
		t.left(90)
t.mysquare(25)
t.mysquare(50)
t.mysquare(75)
t.mysquare(100)
t.mysquare(125)

