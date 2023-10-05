def sum_of_digits(num):
	result=0
	temp=num
	
	while temp>0:
		digit=temp%10
		result+=digit
		temp=temp//10
	print(result)

sum_of_digits(203905)
