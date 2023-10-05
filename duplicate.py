# def find_duplicate(arr):
# 	occurence={}
# 	duplicate=[]
# 	for num in arr:
# 		if num in occurence:
# 			duplicate.append(num)
# 		else:
# 			occurence[num]=1
# 	return duplicate



def find_duplicates(arr):
    duplicates = []
    for num in arr:
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates
input_value=[2,3,0,4,5,5,3,44,2,4,2,4,]

print(find_duplicates(input_value))
