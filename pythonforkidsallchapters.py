#Python For Kids Ch2 Variables, Ch3 My Letter or composing a string, Ch5 Asking Questions With If And Else, Ch6 Going Loopy or for and while loops, 

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
