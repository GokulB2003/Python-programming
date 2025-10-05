ch=(input("Enter the character"))
if(ch>='a' and ch<='z'):
	h=ord(ch);
	p=ord('z')
else:
	h=ord(ch);
	p=ord('Z')	

while(h<=p):
	print(chr(h),end=" ");
	h=h+1;
	
