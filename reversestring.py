def reverse(string):
	reversed_string=""
	for i in string:
		reversed_string=i+ reversed_string

	if string==reversed_string:
		print(string,"is a palindrome")
	else:
		print(string,"is not a palindrome")
	return reversed_string
		


reverse("malini")

