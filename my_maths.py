#my_maths.py
def calculate():
    print("choose any type of mathematical signs to calculate for you")
    print("A.add")
    print("B.subtract")
    print("C.multiply")
    print("D.divide")
    x=int( input("enter first number:"))
    z=int( input("enter second number:"))

    y=input("enter your chioce:")
    if y=="A":
     
     result=x+z
     print("Your answer is: ",result)
    elif y=="B":
     x=int( input("enter first number: "))
     z=int( input("enter second number: "))
     result=x-z
     print("Your answer is: ",result)
    elif y=="C":
     x=int( input("enter first number: "))
     z=int( input("enter second number: "))
     result=x*z
     print("Your answer is: ",result)
    elif y=="D":
     x=int( input("enter first number: "))
     z=int( input("enter second number: "))
     result=x/z
     print("Your is: ",result)
    else:
     print("invalid input, please retry")
     y=input("enter your chioce: ")

calculate()



