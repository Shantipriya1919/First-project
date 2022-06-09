a=input("Enter the string1 ")                                 #"silent"
b=input("Enter the string2 ")                                #"listen"
x=[a[i] for i in range(len(a))]					#x=sorted(a)
x.sort()
y=[b[i] for i in range (len(b))]
y.sort()

if (x==y):
	print("The strings are anagrams")
else:
	print("The strings are not anagrams")
