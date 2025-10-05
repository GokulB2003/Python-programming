#Q52. Print the middle value among 3 distinct integers.
a=(int(input("Enter the value of a:")))
b=(int(input("Enter the value of B:")))
c=(int(input("Enter the value of c:")))
if (a>b and a<c) or(a>c and a<b):
	print("middle:",a);
elif (b>a and b<c) or (b<a and b>c):
	print("middle:",b);
else:
	print("middle:",c);