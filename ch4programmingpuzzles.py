#1 a rectangle
import turtle

t=turtle.Pen()
t.reset() #erase canvas, turtle returns to starting position
t.clear() #erase canvas, turtle remains in position
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)

#2 a triangle
t=turtle.Pen()
t.reset() #erase canvas, turtle returns to starting position
t.clear() #erase canvas, turtle remains in position
t.forward(8)
t.left(135)
t.forward(10)
t.left(135)
t.forward(6)
t.left(90)

#3 a box without corners
t=turtle.Pen()
t.reset() #erase canvas, turtle returns to starting position
t.clear() #erase canvas, turtle remains in position
t.forward(50)
t.up()
t.forward(25)
t.left(90)
t.forward(25)
t.down()
t.forward(50)
t.up()
t.forward(25)
t.left(90)
t.forward(25)
t.down()
t.forward(50)
t.up()
t.forward(25)
t.left(90)
t.forward(25)
t.down()
t.forward(50)
t.up()
t.forward(25)
t.right(270)
t.forward(25)