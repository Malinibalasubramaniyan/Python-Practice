def reverse_sentence(sentence):
	words=sentence.split()
	reverse=words[::-1]
	reversed_sentence=" ".join(reverse)
	return reversed_sentence

word="hello world"

output=reverse_sentence(word)

print(output)