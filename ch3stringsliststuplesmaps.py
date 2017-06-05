fred = "Why do gorillas have big nostrils?  Big fingers!!"
print(fred)
fred = 'What is pink and fluffy?  Pink fluff!!'
print(fred)

#\n is a line break, start a new line
jane = "How do dinosaurs pay their bills?\nWith tyrannosaurus checks!"
print(jane)
jane2 = "How do dinosaurs pay their bills?\n With tyrannosaurus checks!"
print(jane2)
print("\n")

quote = "I think I'm okay"
print(quote)
quote2 = 'I think I\'m okay'
print(quote2)
single_quote_str = 'He said, "Aren\'t, can\'t, shouldn\'t, wouldn\'t."'
print(single_quote_str)
double_quote_str = "He said, \"Aren\'t, can\'t, shouldn\'t, wouldn\'t.\""
print(double_quote_str)
print("\n")

myscore = 1000
message = "I scored %s points"
print(message % myscore)
print("I scored %s points" % myscore)

joke_text = "%s: a device for finding furniture in the dark"
bodypart1 = "Knee"
bodypart2 = "Shin"
print(joke_text % bodypart1)
print("%s: a device for finding furniture in the dark" % bodypart1)
print(joke_text % bodypart2)
print("%s: a device for finding furniture in the dark" % bodypart2)

nums = "What did the number %s say to the number %s?  Nice belt!!"
print(nums % (0, 8))
print("What did the number %s say to the number %s?  Nice belt!!" % (0, 8))

print(10 * "a")
#print("snirt" * 1000) #print("snirt" * 1000) also works
print("\n")

wizard_list = ["spider legs","toe of frog","eye of newt","bat wing","slug butter","snake dandruff"]
print(wizard_list)
print(wizard_list[2])
wizard_list[2] = "snail tongue"
print(wizard_list)
print("Let's see the third, fourth, and fifth items:" ,wizard_list[2:5],"It's like [-1:+1]") # plus sign syntax error.  Use comma.
print("\n")

numbers_and_strings = ["Why", "was", 6, "afraid", "of", 7, "because", 7, 8, 9]
print(numbers_and_strings)

numbers = [1, 2, 3, 4]
strings = ["I", "kicked", "my", "toe", "and", "it", "is", "sore"]
mylist = [numbers, strings]
mylist2 = (numbers + strings)
print(mylist)
print("Add lists use plus sign, add text use comma:" ,numbers + strings)
print(mylist2)
print("\n")

twonumbers = [10, 11]
print("Repeat the list five times (remember comma):" ,twonumbers * 5)
print("\n")

wizard_list.append("bear burp")
print(wizard_list)
wizard_list.append("mandrake")
wizard_list.append("hemlock")
wizard_list.append("swamp gas")
print(wizard_list)
print("\n")
del(wizard_list[5])
print(wizard_list)
del(wizard_list[6:9]) #del a list range it appers [0:+1]
print(wizard_list)
print("\n")

#A tuple is like a list uses parentheses.  Tuples can't change.
#Sometimes need a list don't want to change
fibs = (0, 1, 1, 2, 3)
print(fibs[3])
print("\n")

#A map or a dictionary is a collection of things.  Each item in a map has a key and a corresponding value.
#list
favorite_sports_list = ["Ralph William, Football", "Michael Tippett, Basketball", "Edward Elgar, Baseball", "Rebecca Clarke, Netball","Ethel Smyth, Badminton", "Frank Bridge, Rugby"]
print(favorite_sports_list)
print("\n")
#map or a dictionary.  A colon separates each key for its value
favorite_sports = {"Ralph William" : "Football", "Michael Tippett" : "Basketball", "Edward Elgar" : "Baseball", "Rebecca Clarke" : "Netball","Ethel Smyth" : "Badminton", "Frank Bridge" : "Rugby"}
print(favorite_sports)
print(favorite_sports["Rebecca Clarke"])
del(favorite_sports["Ethel Smyth"])
print(favorite_sports)
favorite_sports["Ralph Williams"] = "Ice Hockey"
print(favorite_sports)
#maps can't be combined.