sentence="I am a software engineer"
string=sentence.lower()
print(sentence)
count=0
list_of_sentence=["a","e","i","o","u"]
for i in string:
	if i in list_of_sentence:
		count+=1

print("count",count)
