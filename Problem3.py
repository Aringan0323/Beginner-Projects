#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
#Description: This program prompts the user to enter a word, and then tells
#the user if the word is a palindrome, ie. if it can be spelled the same
#way both fowards and backwards.

def palindrome(s):
	counter = len(s) - 1
	#assignes counter to a number that is one less than the number of letters
	#in the parameter "s".
	for i in range(len(s)):
		#for loop runs through each letter of the parameter "s"
		if s[i] != s[counter]:
			#if the letters equidistant to the middle of the word are 
			#the not the same, the function returns false.
			return False
		counter -= 1
	return True
	#if the for loop is completed without returning false, the function
	#returns true.

def main():
	string = input("Please enter a string:")
	#prompts the user to enter a string.
	print(palindrome(string))
	#applies the palindrome function to the string and then prints the output.

main()