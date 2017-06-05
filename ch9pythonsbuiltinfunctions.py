#Python has programming tools including functions and modules ready-made to use.  Can make writing programs a lot easier.
#Modules need to be imported before they can be used.
#Python's built-in functions don't need to be imported; they're available now.
#Ch9 looks at 12 functions--some of the more useful built-in functions including the open function.

#abs() function
print(abs(-10))
steps = -3
if abs(steps) > 0:
	print("Character is moving")

#bool() function
#boolean for numbers, 0 returns False, any other number returns True
print(bool(0))	
print(bool(159875312.18))
#boolean for other values like strings and lists, no value returns False, otherwise returns True
print(bool(None)) #None "N" must be capitalized
print(bool("yup"))
print(bool(" ")) #returns True
my_silly_list = []
print(bool(my_silly_list))
#rstrip() function removes spaces and enter characters from the end of the string
year = input("Year of birth: ")
if bool(year.rstrip()) == False:
	print("You need to enter a value for your year of birth.")
else:
	print("You're age" ,year)

#dir() function
#short for directory, returns information about any value.  It tells you the functions used with that value
popcorn = "I love popcorn!"
print(dir(popcorn))

#eval()
#short for evaluation, takes a string as a parameter and runs it as though it were a Python expression
print(eval("10*5"))
#eval() often used to turn user input into Python expressions
your_calculation = input("Enter a calculation: ")
print(eval(your_calculation))

#exec() function
#similar to eval(), exec() doesn't allow to save values in a variable
#exec() can run mini programs

#float()
#convert string to float
print(float(12)) #returns 12.0
print(float("12")) #returns 12.0
print(float("123.456789")) #returns 123.456789
your_age = input("Enter your age: ")
age = float(your_age)
if age > 13:
	print("You are %s too old" % (age - 13))
else:
	print("No worries")

#int()
#convert string or a number into a whole number
print(int("12")) #returns 12
#print(int("123.456789")) #convert a string floating to interger results in error message

#len()
print(len("This is a test string.")) #returns 22.  22 characters including spaces
creature_list = ["unicorn","cyclops","fairy","elf","dragon","troll"]
print(len(creature_list)) #returns 6
enemies_map = {"Batman": "Joker", "Superman": "Lex Luthor", "Spiderman": "Green Goblin"}
print(len(enemies_map)) #returns 3
length = len(creature_list)
for x in range(0, length):
	print("The creature %s is located at %s" % (x, creature_list[x]))

#max() and min()
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
print(min(numbers))
#letters are ranked alphabetically, uppercase before lowercase
strings = "s,t,r,i,n,g,S,T,R,I,N,G"
print(max(strings)) #returns t
print(min(strings)) #returns ,

#range()
#range(low,high-1,step)
#range returns an iterator that repeat an action a number of times.  In this case, it returns the next highest number each time it is called
for x in range(0,5):
	print(x)
print(list(range(0,5)))
count_down_by_twos = list(range(40,10,-2))
print(count_down_by_twos) #returns 40, 38, 36, . . . ,16, 14, 12

#sum()
count_down_by_twos = list(range(40,10,-2))
print(sum(count_down_by_twos))

#open()
#open a file
test_file = open("test.txt")
text = test_file.read()
print(text)

#write()
#write to a fil
#the file object returned by open has other functions besides read.  We can create a new empty file by using a second parameter, the string "w" when calling the function.
#"w" tells Python we want to write to the file object instead of reading
test_file = open("text.txt", "w")
test_file.write("this is new test")

#close()
#we need to tell Python when we're finished writing to the file using the close() function
test_file.close()