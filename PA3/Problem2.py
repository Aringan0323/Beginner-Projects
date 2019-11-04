#Adam Ring
#COSI 10a, Fall 2019
#Programming assignment #3
#
#Description: This program asks the user to input 3 integer values, and then returns the factorial of each integer value

def main():
	
	#A for loop cycles 3 times
	for z in range(1,4):

		#The program asks the user to enter an integer
		i = int(input("Enter a integer:"))
		
		#the counter variable f is set equal to 1
		f = 1

		#A for loop cycles i times, starting at 1 and ending at i+1
		for x in range(1,i+1):

			#Each time the loop cycles, f is multiplied by the number of times the loop has cycled
			f = f * x

		#The program outputs the input factorial, and then repeats 
		print(i,"! = ",f)

main()