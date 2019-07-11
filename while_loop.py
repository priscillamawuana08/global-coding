#creating a while_loop
i = 0
while(i < 10):
    i = i + 1
    print (i)
#This code above means that any number put into the equation 
#will be equal i which should be less than 10 or equal to 10.

print(" ")
#printing numbers  from 7 to 19.
for x in range (7,20):
    print(x)


print(" ")
#printing even numbers between 12 and 20.
for x in range (14,20,2):
    print(x)

print(" ")
print(" ")
#create a function called "even"that takes two numbers and print 
#all even  numbers between them.
def even():
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    for n in range(x,y):
      if n % 2 == 0:
          print(n,"is even")

even()


print(" ")
#create a function called "even"that takes two numbers and print 
#all even  numbers between them.
def reversedeven():
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    for n in reversed(range(x,y)):
      if n % 2 == 0:
          print(n,"is even")

reversedeven()

