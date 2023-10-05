def find_missing_array(arr1,arr2):
	set1=set(arr1)
	set2=set(arr2)
	missing_array=set1-set2
	return missing_array

arr1=[2,4,5,6,5,10,9]
arr2=[2,3,4,6,8,7]

print(find_missing_array(arr1,arr2))