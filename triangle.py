'''
Author:Parvathy J Nair
Description:A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle.
 Implement using functions.
 '''
def right_triangle():
    a=int(input("Enter side-1:"))
    b=int(input("Enter side-2:"))
    c=int(input("Enter side-3:"))
    side=[a,b,c]
    side.sort()
    if side[2]**2==side[1]**2+side[0]**2:
        print ("Right angled triangle")
    else:
        print("Not right angled")
right_triangle()
