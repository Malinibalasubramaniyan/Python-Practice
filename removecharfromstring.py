def remove_char(string,char_to_remove):
	result=""
	for char in string:
		if char!=char_to_remove:
			result+=char
	return result

input_char="Heloo World"
remove="o"
output=remove_char(input_char,remove)

print(output)
