#Write a for loop that sums the values 1 through end, inclusive. end is a 
#variable that we define for you. So, for example, if we define end to be 6, your code should print out the result: 21

total = 0
i = 0
while i <= end:
    total += i
    i += 1

print(total)

#Convert the following into code that uses a while loop.
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2

print("Hello!")
x = 10

while(x >= 2):
    print(x)
    x -= 2
    
    x = 2
    
#Convert the following into code that uses a while loop.
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!

while(x <= 10):
    print(x)
    x += 2
else:
    print("Goodbye!")
