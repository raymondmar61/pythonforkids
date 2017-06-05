#1 basic moon weight function
weight = 30
conversion = 0.25
def moonweight(weight, conversion):
	weight = weight * conversion
	for n in range(1,16):
		print("Year",n,weight)
		weight = weight + 1
moonweight(weight, conversion)

#2 moon weight function and years
weight = 30
conversion = 0.25
years = 5
def moonweight(weight, conversion, years):
	weight = weight * conversion
	for n in range(1,years+1):
		print("Year",n,weight)
		weight = weight + 1
moonweight(weight, conversion, years)

#3 moon weight program
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