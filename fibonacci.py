# number=6
# first=0
# second=1
# for x in range(number):
# 	print(first)
# 	temp=first
# 	first=second
# 	second=temp+second

def fibonacci(n):
	fib_series=[0,1]
	for x in range(2,n):
		next_term=fib_series[-1]+fib_series[-2]
		fib_series.append(next_term)
	return fib_series

print(fibonacci(10))


	