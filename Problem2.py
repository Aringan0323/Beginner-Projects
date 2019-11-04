#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
#Description: This program prompts the user to enter both a string
#and a number. It then prints the string with each letter multiplied that
#number of times.

def multiplier(word,multi):
	#Function multiplier takes in both the number that the user entered and
	#the string.
	length = len(word)
	for i in range(length):
		#for loop goes through each letter of the word and multplies it 
		#by the number the user entered, and then prints the multiplied 
		#string.
		a = word[i]
		print(multi * a, end="")

def main():
	word = input("Please enter a string:")
	multi = int(input("Please enter a multiplier for each character to repeat:"))
	#prompts the user for a word and a multiplier.
	multiplier(word,multi)
	#applies the multipier function to the word.

main()