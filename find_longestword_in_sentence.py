def find_longestword(string):
	words=string.split()
	longestword=max(words,key=len)
	return longestword

input_string="The quick brown fox jumps over the lazy dog"
longestword = find_longestword(input_string)

print(input_string)
print(longestword)