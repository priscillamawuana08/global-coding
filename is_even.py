

#a function that takes a number and returns true if it's true which prints 
#the even numbers.
def is_even():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    for i in numbers:
     if i % 2 ==0:
       print(i,"true")
is_even()



#using lambda  to print out even numbers.
numbers = [1,56,234,87,4,76,24,69,90,135]
print(filter(lambda x:x % 2 ==0,numbers))

print(" ")

#codes that will print out all the odd numbers in the list
def odd():
  numbers = [1,56,234,87,4,76,24,69,90,135]
  for a in numbers:
   if a % 2 !=0:
    print(a,"true it's odd")
odd()
