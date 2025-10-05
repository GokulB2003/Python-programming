a=int(input("Enter a"));
b=int(input("b"));
c=int(input("c"));
d=int(input("d"));

...
#if a>10 and a>c:
#	print("a is greater:");
#elif b>a and b>c:#
	#print("b is greater");
#else:
#	print("c is greater:");

...
if a>b:
	if b>c:
		if c>d:
			print("c is greater");
		else:
			print("d is less than c:");...

#ternary
no=int(input("enter no:"))
result="Even" if no%2==0 else "odd";
print(result);