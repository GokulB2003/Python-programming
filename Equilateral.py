'''
 Write a python program to check whether a triangle is equilateral , isoscale  or scalene.
'''
angle1=int(input("Enter the angle1:"))
angle2=int(input("Enter the second angle:"))
angle3=int(input("Enter the third angle:"))
if (angle1==angle2 and angle2==angle3):
	print("Equilateral");
elif (angle1==angle2 and angle2!=angle3) or (angle2==angle3 and angle1!=angle3):
	print("isoscale")
else:
	print("scalene");