#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
#Description: This program asks the user for an integer value, It then 
#applies a function to the integer that determines whether it is odd or 
#even. If the integer is odd, it multiplies it by three and adds 1. If it 
#is even, it divides it by two. Each sequential number is printed, and 
#once the number reaches 1, the program prints how many iterations the 
#number had to go through to get to 1.

def run(n):
	counter = 0
	#counter starts at 0
	while n > 1:
		#while loop ensures that the number has not yet reached 1.
		if (n % 2) == 0:
			#if statement determines if the number is even.
			n /= 2
			#sets the number to itself divided by 2.
		else:
			n = (n * 3) + 1
			#if the number is something other than even (odd), then the
			#function sets it to itself times 3 plus 1.
		counter += 1
		#counter increases by one after every iteration.
		if n > 1:
			print("The next value is:", n)	
			#prints the current value if it is greater than 1.
	print("Final value ", n,", number of operations performed ", counter)
	#once the number reaches 1, it prints the final value (1) and the number
	#of iterations that it took to produce it.

def main():
	number = int(input("Initial value is:"))
	#prompts the user for the initial value.
	run(number)
	#runs the number through the algorithm.

main()
