import math

#calculating area of a circle with lambda and function.
def arearadii (r):
    area = math.pi*r**2
    radii = [2,3,4,5,6]
print (list(map(area,radii)))

#the use of filter to print negative numbers.
list=[-2,-1,]
print(filter(lambda a:a<0,list))
