def prime(num):
	if num<=1:
		return False

	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False

	return True

num=16
if prime(num):
	print(num,"is prime")
else:
	print(num,"is not prime")
	