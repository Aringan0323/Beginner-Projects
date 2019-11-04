#Problem 1

def main():

	#The program prompts the user to enter an integer value
	i = int(input("Enter an exponent:"))

	#A for loop prints increasing powers of 2 based on what the user entered as an input
	for x in range(0, (i+1)):
		print(2**x)

main()