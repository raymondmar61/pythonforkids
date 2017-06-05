#A Python module is any combination of functions, classes, and variables.  Python uses modules to group functions and classes; e.g. the turtle module groups functions and classes to create a canvas for a turtle to draw on screen.

#copy
#The copy module contains functions for creating copies of objects.  It's useful to create a copy of an object, and then use that copy to create a new object.
#an Animal class with __init__ function takes parameters name, number of legs, and color
class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
#create a new object called harry in the Animal class 
harry = Animal("hippogriff",6,"pink")
import copy
#create a copy of harry object called harriet
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)
print(harry.color)
print(harriet.color)
carrie = Animal("chimera",4,"green polka dots")
billy = Animal("bogill",0,"paisley")
my_animals = [harry, carrie, billy]
#copy list my_animals to create a new list more_animals
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
#change harry's species from hippogriff to ghoul
#my_animals and more_animals lists print ghoul
#copy makes a shallow copy which means it doesn't copy objects inside the objects we copied
my_animals[0].species = "ghoul"
print(my_animals[0].species) #ghoul
print(more_animals[0].species) #ghoul
#on the other hand, add a new animal to the first list my_animals, it doesn't appear in the copy list more_animals
sally = Animal("spinx",4,"sand")
my_animals.append(sally)
print(len(my_animals)) #4
print(len(more_animals)) #3 because sally not in more_animals list
#another copy module function, deepcopy, actually creates copies of all objects inside the object being copied
#changes to one of our orginal Animal objects don't affect the objects in the new list
more_animals = copy.deepcopy(my_animals)
my_animals[0].species = "wyrm"
print(my_animals[0].species) #wyrm
print(more_animals[0].species) #ghoul
#in my words, shallow copy changes made to original list changes copy list.  deepcopy changes made to origina list doesn't change copy list

#keyword
#a Python keyword is any word in Python which is part of the language itself; e.g. if, else, and for
#the keyword module contains a function named iskeyword and a variable called kwlist
#iskeyword returns True if any string is a Python keyword
import keyword
print(keyword.iskeyword("if")) #True
print(keyword.iskeyword("ozwald")) #False
#the kwlist variable returns a list of all Python keywords
print(keyword.kwlist)

#random
#The most useful functions in the random module are randint, choice, and shuffle
import random
print(random.randint(1,100))
print(random.randint(100,1000))
print(random.randint(1000,5000))
#simple guessing game
#the while loop loops forever.  Stops when player guesses the number
# num = random.randint(1,100)
# while True:
# 	guess = int(input("Guess a number between 1 and 100 "))
# 	if guess == num:
# 		print("You guessed right")
# 		break
# 	elif guess > num:
# 		print("Try lower")		
# 	elif guess < num:
# 		print("Try higher")
#use choice function to pick a random item from a list
desserts = ["ice cream","pancakes","brownies","cookies","candy"]
print(random.choice(desserts))
#the shuffle function mixes up items
random.shuffle(desserts)
print(desserts)

#sys
#The sys module contains system functions to control the Python shell itself
#We look at exit function, stdin object, stdout object, and version variable
import sys
#exit function stopps Python shell or console.  A prompt asks user if want to exit.
sys.exit()
#stdin or standard input propts a user to enter information to be read into the shell and used by the program.  It works like an input() function
v = sys.stdin.readline()
print(v)
#you can specificy the number of charactesr to read as a parameter.  This works only in the console, not running in the shell
v = sys.stdin.readline(13)
print(v)
#stdout or standard output writes messages to the shell or console rather than reading them.  It's like print.  stdout is a file object
sys.stdout.write("What does a fish say when it swims into a wall?  Dam.")
#version displays your version of Python
print(sys.version)

#time
#The time module contains functions for displaying the time
import time
print(time.time()) #prints number of seconds since Jan 1, 1970
#example
def lots_of_numbers(max):
	t1 = time.time()
	for x in range(0,max):
		print(x)
	t2 = time.time()
	print("It took %s seconds to print" % (t2-t1))
#the function asctime takes a date as a tuple and converts it into something more readable
print(time.asctime())
#to call asctime() with a parameter, we create a tuple with values for the date and time
t = (2007, 5, 27, 10, 30, 48, 6, 0, 0) #year, month, day, hours, minutes, seconds, day of the week (0 = Mon, 1 = Tue), day of the year (put 0 as placeholder), and whether or not it's daylight savings (0 = no, 1 = yes)
print(time.asctime(t))
#localtime() function returns the current date and time as an object
print(time.localtime())
#to print the current year and month, use the index positions.  year is first position [0] and month is second position [1]
t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)
#sleep() function is used to delay or slowdown your program in seconds
for x in range(0,61):
	print(x)
	time.sleep(1)

#pickle
#The pickle module converts Python objects into something that can be written into a file and then easily read back out.  Pickle is useful writing a game and want to save informaiton about a player's progress	