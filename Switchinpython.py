#switch in python
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("1Addition ")
print("subtraction")
print("multiplication")
print("Division:")
choice=int(input("Enter the number "))
match choice:
	case 1:
		print("Add:",a+b)
			
	case 2:
		print("sub",a-b)
		#break;
	case _:
		print("wrong choice:")
