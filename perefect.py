def perfect(num):
	if num<=1:
		return False

	sum_of_divisior=0
	for i in range(1,num):
		if num%i==0:
			sum_of_divisior=sum_of_divisior+i
	return sum_of_divisior==num

num=28
if perfect(num):
	print(num,"is perfect")
else:
	print(num,"is not perfect")


