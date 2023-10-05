arr=[1,2,6,34,67,2,5,1]
max1=arr[0]
n=len(arr)
for i in range(1,n):
	if arr[i]>max1:
		max1=arr[i]
print("max",max1)

min1=arr[0]
for i in range(1,n):
	if arr[i]<min1:
		min1=arr[i]
print("min",min1)


	