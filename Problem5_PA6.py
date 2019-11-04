#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
# Description: This program prompts a user to enter a message consisting of
#a lettered string, and then prompts them to enter a number to encode the
#message with. The program then takes each letter of the message and shifts
#it over the encoding number places in the alphabet. The function then prints
#the encoded message.

def cipher(message, code):
	#The function cypher takes in two parameters, message and code, to
	#encode the message.
	word = message.upper()
	#converts the message to all uppercase letters
	for i in range(len(word)):
		#for loop runs through each letter in the word
		n = word[i]
		value = ord(n) + code
		#converts the letter and the code to a number
		if value <= 90:
			n = chr(value) 
			#translates the number back into a character
			print(n, end="")
		else:
			#wraps the letters at the end of the alphabet back to the beginning.
			value = 64 + (value % 90)
			n = chr(value)
			print(n, end="")

def main():
	word = str(input("Please enter a word to encode:"))
	shift = int(input("Please indicate the number of spots to shift each letter:"))
	cipher(word, shift)

main()
