def character_occurence(string,char_to_count):
	count=0
	for char in string:
		if char==char_to_count:
			count+=1
	return count

input_char="heloo"
count_char="o"
output=character_occurence(input_char,count_char)

print(output)