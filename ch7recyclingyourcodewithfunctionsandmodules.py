print(range(0,5))
print(list(range(0,5)))
list(range(0,5)) #nothing appears
#print(list(range(0,1000)))
# for x in range(1,1001):
# 	print(x)

#functions are code telling Python to do something.  They're one way to reuse code--use functions in programs again and again.
#a function has three parts:  name, parameters, and body.
#def is short for define:  def name(parameters): body
firstname = "Raymond"
lastname = "Mar"
def testfunc(firstname, lastname):
	print(firstname+" "+lastname)
testfunc(firstname, lastname)

#a function is often used to return a value, using a return statement.
#the return which can be assigned to a variable
pocketmoney = 5
paperroute = 10
spending = 7
def savings(pocketmoney, paperroute, spending):
	return (pocketmoney + paperroute - spending)
print(savings(pocketmoney, paperroute, spending))

#a variable inside the body of a function can't be used again when the function has finished running because it exists only inside the function.  This is called scope.
def variable_test():
	first_variable = 10
	second_variable = 20
	return (first_variable * second_variable)
print(variable_test()) #make sure variable_test() includes the paranthesis calling function

#if a variable is defined outside the function, it has a different scope
outsidevariable = 100
def variable_test2():
	first_variable = 10
	second_variable = 20
	return (first_variable * second_variable) * outsidevariable
print(variable_test2()) #make sure variable_test2() includes the paranthesis calling function

def spaceship_building(cans):
	total_cans = 0
	for week in range(1, 53):
		total_cans = total_cans + cans
		print("Week %s = %s cans" % (week, total_cans))
spaceship_building(2)

#modules are used to group functions, variables, and other things together into larger, more powerful programs.
#some modules are built in to Python, and you can download other modules separately.
#e.g. import time is the built-in module time; import sys is the system module which contains utilities for interacting with the Python system itself
#import sys
#print(sys.stdin.readline()) #readline() read a line of text typed until you press ENTER.  Type words, press ENTER, words are printed out.  Returns a string.

import sys
def silly_age_joke(age):
	if (age >=10 and age <=13):
		print("What is 13 + 49 + 84 + 155 + 97?  A headache!")
	else:
		print("Huh?")
print("How old are you?")
age = int(sys.stdin.readline())
silly_age_joke(age)

