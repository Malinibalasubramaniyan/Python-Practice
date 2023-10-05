def armstrong(number):
	n=len(str(number))
	result=0
	temp=number
	while temp>0:
		digit=temp%10
		result=result+digit**n
		temp=temp//10
		if number==result:
			print(result,number)
armstrong(153)

# for i in range(1001):
# 	num=i
# 	result=0
# 	n=len(str(i))
# 	while(i!=0) :
# 		digit=i%10
# 		result=result+digit**n
# 		i=i//10
# 	if num==result:
# 		print(num)

	