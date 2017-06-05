age = 25
if age > 20:
	print("You are too old!")
	print("Why are you here?")
	print("Why aren\'t you mowing a lawn or sorting papers?")

age = 10
if age >= 10:
	print("You are too old for my jokes!")

print("Want to hear a dirty joke?")
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
	print("Breathe! Breathe!")
elif age == 12:
	print("What did 0 say to 8?")
	print("Hi guys!")
elif age == 13:
	print("Why wasn't 10 afraid of 7?")
	print("Because rather than eating 9, 7 8 pi.")
else:
	print("Huh?")

# age = int(input("How old are you? "))
# if age == 10:
# 	print("What do you call an unhappy cranberry?")
# 	print("A blueberry!")
# elif age == 11:
# 	print("What did the green grape say to the blue grape?")
# 	print("Breathe! Breathe!")
# elif age == 12:
# 	print("What did 0 say to 8?")
# 	print("Hi guys!")
# elif age == 13:
# 	print("Why wasn't 10 afraid of 7?")
# 	print("Because rather than eating 9, 7 8 pi.")
# else:
# 	print("Huh?")

#We can assign numbers, strings, lists to a variable.
#We can also assign nothing, or an empty value, to a variable.
myval = None
print(myval)
#Assigning a value of None to a variable is one way to reset it to its original, empty state.  It's also a way to deinfe a variable without setting its value.
if myval == None:
	print("The variable myval doesn't have a value")
