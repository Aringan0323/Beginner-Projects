#Adam Ring
#COSI 10a, Fall 2019
#Programming assignment #3
#
#Description: This program prints an ASCII picture on multiple lines

def main():

	#main function starts with assigning a value to the counter variable k
	k=7

	#A for loop counts up to 7 from 1
	for line in range(1, 7):
		print()

		#Every time the for loop is cycled, k decreases by 1
		k = k-1

		#The number of stars printed is determined by the current value of k
		for star in range(1,k):
			print("*", end='')

		#The number of spaces printed is determined by the line number
		for space in range(line):
			print(" ", end='')

		#The number of foward slashes printed is determined by a function with k as the input
		for foslash in range(2*(k-1)):
			print("/", end='')

		#The number of backslashes printed is determined by a function with the line number as the input
		for baslash in range((line-1)*2):
			print("\\", end='')

		#The same number of spaces and stars as previously previous in this line are reprinted in reverse order
		for space in range(line):
			print(" ", end='')
		for star in range(1,k):
			print("*", end='')

main()