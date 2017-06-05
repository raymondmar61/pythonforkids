#1 the hello loop
for x in range(0, 20):
	print("Hello %s" % x)
	print("Hello" ,x)
	if x < 9:
		break #code breaks after printing Hello 0

#2 even numbers or odd numbers.  create a loop pritning up to your year in age
age = 2
while age <= 42:
	print(age)
	age += 2

#3 my five favorite ingredients
ingredients = ["snails", "leeches", "gorilla belly-button line", "caterpillar eyebrows", "centipede toes"]
for x in range(0,5):
	print(x+1,""+ingredients[x])

#4 your weight on the moon
weight = 189
conversion = 0.165
weight = weight * conversion
for n in range(1,16):
	print("Year",n,weight)
	weight = weight + 1
