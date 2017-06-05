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

#draw two parallel lines
t.reset()
t.backward(100)
t.up() #pick up the pen and stop drawing
t.right(90)
t.forward(20)
t.left(90)
t.down() #put down the pen and start drawing
t.forward(100)