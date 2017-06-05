#Take a more graphical approach to objects and classes
#we create two turtle objects avery and kate out of the Pen() class
#avery and kate are members of the Pen() class

#use turtle module
#use python shell.  Type "python3.5".  Next type "import turtle".
import turtle
avery = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate = turtle.Pen()
kate.left(90)
kate.forward(100)
#we have a line with arrowheads moving in two different directions.  Avery went up and Kate went down.  Let's add another turtle jacob
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
#every time we call turlte.Pen() to create a turtle, we add a new independent object.  Each object is still an instance of the class Pen, and we can use the same functions on each object.
#we're using objects.  We can use each object independently.

#classes and objects make it easy to group functions