a=[];
size=int(input("Enter the size of the array"))
i=0;
while i<size:
	val=int(input(""))
	a.append(val);
	i+=1;
i=0;
max=0;
while i<size:
	if a[i]>max:
	max=a[i];
	i=i+1;
