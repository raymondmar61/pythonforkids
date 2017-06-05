#1 the giraffe shuffle
class Giraffes():
	def leftfootforward(self):
		print("left foot forward")
	def leftfootbackward(self):
		print("left foot backward")
	def rightfootforward(self):
		print("right foot forward")
	def rightfootbackward(self):
		print("right foot backward")
	def dance(self):
		self.leftfootforward()
		self.leftfootbackward()
		self.rightfootforward()
		self.rightfootbackward()
		self.leftfootbackward()
		self.rightfootbackward()
		self.rightfootforward()
		self.leftfootforward()
#When we're creating functions inside a class, we refer to the same variables and other functions using the self parameter

reginald = Giraffes()
reginald.dance()

#2 turtle pitchfork
#use turtle module
#use python shell.  Type "python3.5".  Next type "import turtle".
import turtle
t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()
t1.forward(100)
t1.left(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t2.forward(110)
t2.left(90)
t2.forward(25)
t2.right(90)
t2.forward(25)
t3.forward(110)
t3.right(90)
t3.forward(25)
t3.left(90)
t3.forward(25)
t4.forward(100)
t4.right(90)
t4.forward(50)
t4.left(90)
t4.forward(50)
