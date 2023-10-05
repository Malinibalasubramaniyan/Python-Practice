def sum_of_digits(number):
	result=0
	while number>0:
		digit=number%10
		result+=digit
		number=number//10
	print(result)

sum_of_digits(20220671)