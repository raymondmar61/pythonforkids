#1 mystery code
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)

#2 a hidden message
string = "this if is you not are a reading very this good then way you to have hide done a it message wrong"
print(dir(string))
print("I see a funtion called split.  Let's take a look at use it.")
#use split()
#an example look up at Python there is a tool already created
words = string.split()
for x in range(0, len(words), 2):
	print(words[x])

#c copying a file
f = open('test.txt')
s = f.read()
f.close()
f = open('output.txt', 'w')
f.write(s)
f.close()