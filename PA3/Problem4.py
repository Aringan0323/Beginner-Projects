#Adam Ring
#COSI 10a, Fall 2019
#Programming assignment #3
#
#Description:This program prompts the user to enter how many columns and rows they want their grid of numbers to be. 
#The program then prints the requested grid of numbers counting up by 1.

def main():

	#The program asks the user to input the number of rows and columns needed for the grid
	rows = int(input("Enter number of rows:"))
	columns = int(input("Enter number of columns:"))

	#This for loop divides the numbers in the grid into the correct number of rows
	for x in range(1, (rows + 1)):

		#This for loop divides the numbers in the grid into the correct number of columns
		for y in range(1, columns + 1):

			#The program prints the row number, and then adds the number of rows to it each time. It repeats this as many times as there are columns.
			print(x,"\t", end='')
			x = (x + rows)

		#This print statement is used to start a new row of numbers
		print()

main()