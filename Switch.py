print("1.Add");
print("2.sub");
a=int(input("a"));
b=int(input("b"));

choice=int(input("Enter choice:"));

match choice:
	case 1:
		print("Add",a+b);
	case 2:
		print("sub",a-b);
	case _:
		print("Wrong choice");