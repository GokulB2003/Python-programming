#Q38. Write a python program to check whether a year is leap year or not.
year=int(input("Enter the yaer:"))
if (year%4==0 and year%100!=0) or (year%400==0):
	print("leap year")
else:
	print("not leap year") 