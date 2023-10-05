number=6
for row in range(number):
	for col in range(number):
		if col==0 or row==number-1 or row==0 or col==number-1:
		    print("*",end="")
		else:
			print(end=" ")

	print()