#a for loop repeats things like other programming statements and blocks of code automatically
#start counting from 0 and stop before reaching 5
#for each number we count, store the value in the variable x
#Python executes the block of code printing "Hello" five times
for x in range(0,5):
	print("Hello",x)

#range creates a list of numbers (low,high-1,increment).
#Actually range() function returns an iterator.
print(list(range(10,20)))

#you can use a list when making for loops
#for each item in wizard_list, store the value in the variable i, and then print the contents of that variable
wizard_list = ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
for i in wizard_list:
	print(i)

hugehairypants = ["huge", "hairy", "pants"]
for i in hugehairypants:
	print(i)
	print(i)

#python enters the first loop and prints an item for the list.  
#Next it enters the second loop and prints all the items in the list at second loop
#Then it continues with first loop printing the next item in the list, and prints the complete list again at second loop
hugehairypants2 = ["huge", "hairy", "pants"]
for i in hugehairypants2:
	print(i)
	for j in hugehairypants2:
		print(j+ " j loop")

found_coins = 20
magic_coins = 70
stolen_coints = 3
coins = found_coins
for week in range(1,52):
	coins = coins + magic_coins - stolen_coints
	print("Week %s = %s" %(week, coins))

#a for loop is a loop of a specific length
#a while loop is a loop used when you don't know ahead of time when it needs to stop looping
#three steps in a while loop:  1 check the condition 2 execute the code in the block 3 repeat
x = 45
y = 80
while x < 50 and y < 100:
	x += 1
	y += 1
	print(x, y)

#another common use of a while loop is to create semi-eternal loops which are loops going on forever, but actuall continues until something happens in the code to break out of it