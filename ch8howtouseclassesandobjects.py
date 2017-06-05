#Objects are defined by classes which we can think of as a way to classify objects into groups; e.g. Things is the main class.  Inanimate and Animate are below Things.  Sidewalks is below Inanimate.  Animals, Mammals, and Giraffes are below Animate.
#Inanimate and Animate are both children to the class Things.  Things is the parent.
#To tell Python a class is a child of another class, we add the name of the parent class in parentheses after the name of our new class:  class Inanimate(Things): pass also class Animate(Things): pass.  Also class Sidewalks(Inanimate): pass and class Mammals(Animals): pass
#We have a giraffe named Reginald.  Reginald is an object.  Reginald belongs to the class Giraffes.  To "introduce" Reginald, we type reginald = Giraffe() which tells Python to create an object in the Giraffes class and assign it to the variable reginald.
#A characteristic is a trait that all of the members of the class (and its children) share.  Animals's characteristics are breathe, move, eat food.  These characteristics can be thought of as actions, or functions--things that an object of that class can do.
#The self parameter in the three functions is a way for one function in the class to call another function in the class (and in the parent class)
class Animals(): #Animate is the parent for Animals().  Since Animate() is not defined, Animals() is blank.  If Animate() class defined, then class Animals(Animate)
	def breathe(self):
		pass
	def move(self):
		pass
	def eat_food(self):
		pass		

#WE can also add functions to the other two classes Mammals and Giraffes.  Each class use the characteristics (the functions) of its parent.
class Mammals(Animals):
	def feed_young_with_milk(self):
		pass
class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		pass

#why use classes and objects?
#reginald is an object.  We can call or run functions provided by his class Giraffes and its parent classes Mammals and Animals.
#We call functions on an object by using the dot operator and the name of the function.
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

#likewise for Reginald's friend Harold.
harold = Giraffes()
harold.move()
reginald.eat_leaves_from_trees()

class Things():
	pass
class Animate(Things):
	pass
class Animals(Animate):
	def breathe(self):
		print("breathing")
	def move(self):
		print("moving")
	def eat_food(self):
		print("eating food")
class Mammals(Animals):
	def feed_young_with_milk(self):
		print("Feeding Young")
class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print("eating leaves")
raymond = Giraffes()
harold = Giraffes()
reginald = Giraffes()
raymond.move()
raymond.breathe()
raymond.feed_young_with_milk()
harold.move()
reginald.eat_leaves_from_trees()
reginald.move()
#raymond, harold, and reginald objects inherit functions from Mammals, Animals, Animate, and Things classes.  Animals class is parent of Mammals class.  Mammals class is parent of Giraffes class.

#classes and objects make it easy to group functions