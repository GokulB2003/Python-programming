# Write a Java program that takes an alphabet character and toggles its case using ASCII values and operators.
#·Example: a → A, Z → z.
ch=(input("Entr the character ch:"))
if ch>='a' and ch<='z':
	str=chr(ord(ch)-32);
	print(str);
else:
	str=chr(ord(ch)+32);
	print(str);
	