#Python For Kids Ch2 Variables, Ch3 My Letter or composing a string, Ch5 Asking Questions With If And Else, Ch6 Going Loopy or for and while loops, Ch7 Recycling Your Code With Functions And Modules, Ch8 How To Use Classes And Objects, Ch9 Python Build-In Functions, Ch3 Strings Lists Tuples Maps, Ch10 Useful Python Modules, 

fred = 100
print(fred) #print 100
john = fred
print(john) #print 100
john = "fred"
print(john) #print fred
foundcoins = 20
magiccoins = 10
stolecoins = 3
print(foundcoins + (magiccoins * 365) - (stolecoins * 52)) #print 3514
stolecoins = 2
print(foundcoins + (magiccoins * 365) - (stolecoins * 52)) #print 3566
print("\n")

spaces = " " * 25
print("%s 12 Butts Wynd" % spaces)
print("%s Twinklebottom Health" % spaces)
print("%s West Snoring" % spaces)
print("\n" * 2)
print("Dear Sir")
print("\n")
print("I wish to report that tiles are missing from the outside toilet roof.\nI think it was bad wind the other night that blew them away.")
print("\n")
print("Regards")
print("Malcolm Dithering")
print("\n")
print("""
		12 Butts Wynd
		Twinklebottom Health
		West Snoring

Dear Sir

I wish to report that tiles are missing from the outside toilet roof.  I think it was bad wind the other night that blew them away.

Regards,
Malcolm Dithering
""")
games = ("sports","board games","music","gym","hiking","cooking")
foods = ("french fries","kiwi","cinnamon rolls","grapes","cranberry")
favorites = (games + foods)
print(favorites) #print ('sports', 'board games', 'music', 'gym', 'hiking', 'cooking', 'french fries', 'kiwi', 'cinnamon rolls', 'grapes', 'cranberry')
building = 3
ninja = 25
tunnel = 2
samurai = 40
print("Battle personnel:" ,(building * ninja) + (tunnel * samurai))
firstname = "raymond"
lastname = "mar"
print("Hi there, %s %s!" % (firstname, lastname))
print("Hi there, " +firstname+ " " +lastname+ "!")
print("\n")

age = 25
if age > 20:
	print("You are too old!")
	print("Why are you here?")
	print("Why aren\'t you mowing a lawn or sorting papers?")
age = 10
if age >=10:
	print("You are too old for my jokes!")
print("What to hear a dirty joke?")
age = 8
if age == 12:
	print("A pig fell in the mud")
else:
	print("Shh.  It's a secret.")
age = 12
if age == 10:
	print("What do you call an unhappy cranberry?")
	print("A blueberry!")
elif age == 11:
	print("What did the green grape say to the blue grape?")
	print("Breathe!  Breathe!")
elif age == 12:
	print("What did 0 say to 8?")
	print("Hi guys!")
elif age == 13:
	print("Why wasn\'t 10 afraid of 7?")
	print("Because rather than eating 9, 7 8 pi.")
else:
	print("Huh?")
myvar = None
print(myvar) #print None
if myvar == None:
	print("The variable myvar doesn't have a value")
twinkies = 600
if (twinkies < 100) or (twinkies > 500):
	print("Too few or too many")
money = 5000
if ((money > 100) and (money < 500)) or ((money > 1000) and (money < 5000)):
	print("okay")
else:
	print("not okay")
ninjas = 51
if ninjas < 10:
	print("I can fight those ninjas!")
elif ninjas < 30:
	print("It'll be a struggle, but I can take 'em")
elif ninjas < 50:
	print("That's tooo many")
else:
	print("idk")
print("\n")

for x in range(0,5):
	print("Hello",x) #print Hello numbers 0-4
print(list(range(10,21))) #print [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
wizardlist = ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
for eachwizardlist in wizardlist:
	print(eachwizardlist)
hugehairypants = ["huge", "hairy", "pants"]
for eachhugehairypants in hugehairypants:
	print(eachhugehairypants)
	print(eachhugehairypants) #print huge huge hairy hairy pants pants
hugehairypants2 = ["huge", "hairy", "pants"]
for eachhugehairypants2 in hugehairypants2:
	print(eachhugehairypants2)
	for j in hugehairypants2:
		print(j+ " j for loop prints all hugehairypants2 then goes back to eachhugehairypants2 for loop")
foundcoins = 20
magiccoins = 70
stolencoints = 3
coins = foundcoins
for week in range(1,53):
	coins = coins + magiccoins - stolencoints
	print(week, "=", coins)
x = 45
y = 80
while x < 50 and y < 100:
	x += 1
	y += 1
	print(x, y) #print 46 81\n 47 82\n 48 83\n 49 84\n 50 85
for x in range(0, 20):
	print("Hello",x)
	if x < 9:
		break #code breaks after printing Hello 0.  0 is less than 9.
age = 2
while age <=42:
	print(age)
	age += 2
ingredients = ["snails", "leeches", "gorilla belly-button line", "caterpillar eyebrows", "centipede toes"]
for eachingredients in ingredients:
	print(eachingredients)
for x in range(0,5):
	print(x+1,""+ingredients[x])
#two for loops above printed all five ingredients
weight = 189
conversion = 0.165
weight = weight * conversion
for n in range(1,16):
	print("Year",n,weight)
	weight += 1
print("\n")

print(range(0,5)) #print range(0,5)
print(list(range(0,5))) #print [0, 1, 2, 3, 4]
def testfunc(firstname, lastname):
	print(firstname+ " " +lastname)
first = "Raymond"
last = "Mar"
testfunc(first, last) #return Raymond Mar
def savings(pocketmoney, paperroute, spending):
	return (pocketmoney + paperroute - spending)
print(savings(5, 10, 7)) #print 8
def variabletest():
	variable1 = 10
	variable2 = 20
	return (variable1 * variable2)
print(variabletest()) #print 200
outsidevariable = 100
def variabletest2():
	variable1 = 100
	variable2 = 200
	return (variable1 * variable2 * outsidevariable)
print(variabletest2()) #print 2000000
def spaceshipbuilding(cans):
	totalcans = 0
	for week in range(1,53):
		totalcans = totalcans + cans
		print("Week %s = %s cans" % (week, totalcans)) #week and totalcans are presented as a string
spaceshipbuilding(2)
#import sys
#print(sys.stdin.readline()) #readline() read a line of text typed until you press ENTER.  Type words, press ENTER, words are printed out.  Returns a string.
#It looks like input()
import sys
def silly_age_joke(age):
	if (age >=10 and age <=13):
		print("What is 13 + 49 + 84 + 155 + 97?  A headache!")
	else:
		print("Huh?")
print("How old are you?")
age = int(sys.stdin.readline())
silly_age_joke(age)
def moonweight(weight, conversion=0.25):
	weight = weight * conversion
	for n in range(1,16):
		print("Year",n,weight)
		weight = weight + 1
moonweight(30)
def moonweight2(weight, conversion, years):
	weight = weight * conversion
	for n in range(1,years+1):
		print("Year",n,weight)
		weight = weight + 1
moonweight2(30,0.25,5)
import sys
print("Please enter your current Earth weight")
weight = int(sys.stdin.readline())
print("Please enter the amount your weight might increase each year")
conversion = float(sys.stdin.readline())
print("Please enter the number of years")
years = int(sys.stdin.readline())
def moonweight(weight, conversion, years):
	weight = weight * conversion
	for n in range(1,years+1):
		print("Year",n,weight)
		weight = weight + 1
moonweight(weight, conversion, years)
# earthweight = int(input("Please enter your current Earth weight "))
# conversionrate = float(input("Please enter the amount your weight might increase each year "))
# yearsrate = int(input("Please enter the number of years "))
# moonweight(earthweight, conversionrate, yearsrate)
print("\n")

class Animals():
	def breathe(self):
		print("breathe")
	def move(self):
		print("I\'m moving")
	def eatfood(self):
		print("Meal time")
yawn = Animals()
yawn.breathe() #return breathe
yawn.move() #return I'm moving
whistle = Animals()
whistle.move() #return I'm moving
whistle.eatfood() #return Meal time
class Mammals(Animals):
	def feed_young_with_milk(self):
		print("Feeding Young")
class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print("eating leaves")
raymond = Giraffes()
raymond.eat_leaves_from_trees() #return eating leaves
raymond.feed_young_with_milk() #return Feeding Young
raymond.breathe() #return breathe
class Giraffesinit:
	def __init__(self, spots):
		self.spots = spots		
ozward = Giraffesinit(100)
print(ozward.spots) #print 100
gertrude = Giraffesinit(150)
print(gertrude.spots) #print 150
print("\n")

print(abs(-3)) #print 3
print(bool(0)) #print False
print(bool(154897)) #print True
print(bool(None)) #print False
print(bool(" ")) #print True
#dir() function
#short for directory, returns information about any value.  It tells you the functions used with that value
popcorn = "I love popcorn!"
print(dir(popcorn))
#eval()
#short for evaluation, takes a string as a parameter and runs it as though it were a Python expression
print(eval("10*5")) #print 50
#float()
#convert string to float
print(float(12)) #print 12.0
print(float("12")) #print 12.0
print(float("123.456789")) #print 123.456789
print(int("12")) #print 12
print(len("This is a test string.")) #print 22
creature_list = ["unicorn","cyclops","fairy","elf","dragon","troll"]
print(len(creature_list)) #print 6
enemies_map = {"Batman": "Joker", "Superman": "Lex Luthor", "Spiderman": "Green Goblin"}
print(len(enemies_map)) #print 3
length = len(creature_list)
for x in range(0, length):
	print("The creature %s is located at %s" % (x, creature_list[x]))
#max() and min()
numbers = [5, 4, 10, 30, 22]
print(max(numbers)) #print 30
print(min(numbers)) #print 4
#letters are ranked alphabetically, uppercase before lowercase
strings = "s,t,r,i,n,g,S,T,R,I,N,G"
print(max(strings)) #print t
print(min(strings)) #print ,
string = "this if is you not are a reading very this good then way you to have hide done a it message wrong"
words = string.split()
print(words) #print ['this', 'if', 'is', 'you', 'not', 'are', 'a', 'reading', 'very', 'this', 'good', 'then', 'way', 'you', 'to', 'have', 'hide', 'done', 'a', 'it', 'message', 'wrong']
for x in range(0, len(words), 2):
	print(words[x])
print("\n")

joke_text = "%s: a device for finding furniture in the dark"
bodypart1 = "Knee"
bodypart2 = "Shin"
print(joke_text % bodypart1) #print Knee: a device for finding furniture in the dark
print("%s: a device for finding furniture in the dark" % bodypart1)
print(joke_text % bodypart2) #print Shin: a device for finding furniture in the dark
print("%s: a device for finding furniture in the dark" % bodypart2)
nums = "What did the number %s say to the number %s?  Nice belt!!"
print(nums % (0, 8)) #What did the number 0 say to the number 8?  Nice belt!!
print("What did the number %s say to the number %s?  Nice belt!!" % (0, 8))
wizard_list = ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
print(wizard_list) #print ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
print(wizard_list[2]) #print eye of newt
wizard_list[2] = "snail tongue"
print(wizard_list) #print ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff']
print("Let's see the third, fourth, and fifth items:" ,wizard_list[2:5],"It's like [-1:+1]") #print Let's see the third, fourth, and fifth items: ['snail tongue', 'bat wing', 'slug butter'] It's like [-1:+1]
numbers = [1, 2, 3, 4]
strings = ["I", "kicked", "my", "toe", "and", "it", "is", "sore"]
mylist = [numbers, strings]
print(mylist) #print [[1, 2, 3, 4], ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']]
mylist2 = (numbers + strings)
print(mylist2) #print [1, 2, 3, 4, 'I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
twonumbers = [10, 11]
print("Repeat the list five times (remember comma):" ,twonumbers * 5) #print Repeat the list five times (remember comma): [10, 11, 10, 11, 10, 11, 10, 11, 10, 11]
wizard_list = ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
wizard_list.append("bear burp")
print(wizard_list) #print ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp']
wizard_list.append("mandrake")
wizard_list.append("hemlock")
wizard_list.append("swamp gas")
print(wizard_list) #print ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp', 'mandrake', 'hemlock', 'swamp gas']
del(wizard_list[5])
print(wizard_list) #print ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'bear burp', 'mandrake', 'hemlock', 'swamp gas']
del(wizard_list[6:9]) #del a list range it appers [0:+1]
print(wizard_list) #print ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'bear burp']
fibs = (0, 1, 1, 2, 3)
print(fibs[3]) #print 2
favorite_sports = {"Ralph William" : "Football", "Michael Tippett" : "Basketball", "Edward Elgar" : "Baseball", "Rebecca Clarke" : "Netball","Ethel Smyth" : "Badminton", "Frank Bridge" : "Rugby"}
print(favorite_sports) #{'Rebecca Clarke': 'Netball', 'Michael Tippett': 'Basketball', 'Frank Bridge': 'Rugby', 'Ethel Smyth': 'Badminton', 'Edward Elgar': 'Baseball', 'Ralph William': 'Football'} no particular order
print(favorite_sports["Rebecca Clarke"]) #print Netball
del(favorite_sports["Ethel Smyth"])
print(favorite_sports) #print {'Rebecca Clarke': 'Netball', 'Michael Tippett': 'Basketball', 'Frank Bridge': 'Rugby', 'Edward Elgar': 'Baseball', 'Ralph William': 'Football'} no particular order
favorite_sports["Ralph Williams"] = "Ice Hockey"
print(favorite_sports) #print {'Ralph Williams': 'Ice Hockey', 'Rebecca Clarke': 'Netball', 'Michael Tippett': 'Basketball', 'Frank Bridge': 'Rugby', 'Edward Elgar': 'Baseball', 'Ralph William': 'Football'} no particular order
#maps can't be combined.
print("\n")

#copy
#The copy module contains functions for creating copies of objects.  It's useful to create a copy of an object, and then use that copy to create a new object.
import copy
class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
harry = Animal("hippogriff",6,"pink")
print(harry.species) #print hippogriff
print(harry.number_of_legs) #print 6
harriet = copy.copy(harry) #create a copy of harry object called harriet
print(harriet.species) #print hippogriff
print(harriet.number_of_legs) #print 6
print(harry.color) #print pink
print(harriet.color) #print pink
carrie = Animal("chimera",4,"green polka dots")
billy = Animal("bogill",0,"paisley")
myanimals = [harry, carrie, billy]
print(myanimals) #print [<__main__.Animal object at 0x7fc7d2505e80>, <__main__.Animal object at 0x7fc7d2505f60>, <__main__.Animal object at 0x7fc7d2505f98>]
print(myanimals[1]) #print <__main__.Animal object at 0x7fc14133cf60>
print(myanimals[1].species) #print chimera
myanimals[1].species = "ghoul"
print(myanimals[1].species) #print ghoul
deepcopymyanimals = copy.deepcopy(myanimals) #another copy module function, deepcopy, actually creates copies of all objects inside the object being copied
print(deepcopymyanimals[1].species) #print ghoul
myanimals[1].species = "zebra"
print(myanimals[1].species) #print zebra
print(deepcopymyanimals[1].species) #print ghoul
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