#Adam Ring
#Cosi 10a, Fall 2019
#Programming Assignment #6
#
#Description: This program is a full game of rock paper scissors with 4 playable modes.
#The user can choose between easy, medium, hard, or very hard mode, and 
#play against the computer. The program will alert the player who won, and
#in one mode, even use the player's past moves to gain an edge in the game.

import random
#Imports python's random library to assist with the CompShoot_rand function.

def CompShoot_easy(user):
	#this function sees the user's input and and will automatically pick the losing move every time.
	r = "ROCK"
	p = "PAPER"
	s = "SCISSORS"
	if user == r:
		compshoot = s
	elif user == p:
		compshoot = r
	elif user == s:
		compshoot = p
	return(compshoot, user)

def CompShoot_rand(user):
	#This function chooses rock, paper, or scissors completely randomly by assigning each move to a number 1 through 3, and then picking the move that
	#corresponds to the output of python's random number generator.
	compshoot = random.randint(1,3)
	if compshoot == 1:
		compshoot = "ROCK"
	elif compshoot == 2:
		compshoot = "PAPER"
	else:
		compshoot = "SCISSORS"
	return(compshoot, user)

def CompShoot_strat(user, userpast, cond):
	#This function works on a principle of psychology and game theory that suggests that if a player loses a turn of rock paper scissors, they
	#will change their next move. If they win a turn, they will stick with their previous move.
	r = "ROCK"
	p = "PAPER"
	s = "SCISSORS"
	if cond == 0:
		#The condition equaling 0 corresponds to the player losing the previous turn. The computer assumes that the defeated player will change their
		#move in the next turn, so it chooses the move that will either tie the game or win the game for the computer if the player changes their move.
		if userpast == r:
			compshoot = s
		if userpast == p:
			compshoot = r
		if userpast == s:
			compshoot = p
	else:
		#The condition equaling 1 corresponds to the player winning the previous turn. The computer assumes that the  player will not change their
		#move in the next turn, so it chooses the move that will win the game for the computer if the player sticks to their move.
		if userpast == r:
			compshoot = p
		elif userpast == p:
			compshoot = s
		elif userpast == s:
			compshoot = r
	return(compshoot, user)

def CompShoot_impossible(user):
	#This function sees the user's input and will automatically pick the winning move every time.
	r = "ROCK"
	p = "PAPER"
	s = "SCISSORS"
	if user == r:
		compshoot = p
	elif user == p:
		compshoot = s
	elif user == s:
		compshoot = r
	return(compshoot, user)

def User_Shoot():
	#This function prompts the user to enter either rock, paper, or scissors, and then converts the string to uppercase to be returned.
	usershoot = "arbitrary string"
	while usershoot != ("ROCK" or "PAPER" or "SCISSORS"):
		usershoot = str(input("Enter \"Rock\", \"Paper\", or \"Scissors\": "))
		usershoot = usershoot.upper()
	return(usershoot)

def Decide(compu):
	lose = "the computer wins."
	win = "you win!"
	c = "The computer chose " + compu[0].lower() + ","
	r = "ROCK"
	p = "PAPER"
	s = "SCISSORS"
	#Variables are assigned to strings in order to streamline the function.
	comp = compu[0]
	user = compu[1]
	#extracts the user and computer moves in order to determine whether the computer or the user won the round.
	if comp == user:
		print(c)
		print("it was a tie!")
		return(0)
	elif comp == r:
		if user == p:
			print(c)
			print(win)
			return(1)
		elif user == s:
			print(c)
			print(lose)
			return(0)
	elif comp == p:
		if user == r:
			print(c)
			print(lose)
			return(0)
		elif user == s:
			print(c)
			print(win)
			return(1)
	elif comp == s:
		if user == r:
			print(c)
			print(win)
			return(1)
		elif user == p:
			print(c)
			print(lose)
			return(0)
	#If/then statements determine who won the round.

def choose_mode():
	i = str(input("Type whether you would like to play \"easy\", \"medium\", \"hard\" or \"very hard\" mode: "))
	#prompts the user to enter a mode that they want to play.
	if i == "easy":
		play = "yes"
		while play == "yes":
		#while statement 
			Decide(CompShoot_easy(User_Shoot()))
			#decide statement takes in the computer's move from the respective mode and the user's move.
			play = str(input("Type \"yes\" to play this mode again,\nor type anything else to return to the main menu: "))
			#At the end of each round, it prompts the user to enter yes if they want to play again.
	elif i == "medium":
		play = "yes"
		while play == "yes":
			Decide(CompShoot_rand(User_Shoot()))
			play = str(input("Type \"yes\" to play this mode again,\nor type anything else to return to the main menu: "))
	elif i == "hard":
		play = "yes"
		strat = "ROCK"
		#Assumes the initial user input in the strtegy to be rock (statistically, most players choose rock as their first move in this game)
		condition = 1
		#sets the condition to 1 before the while statement begins (fence-post algorithm)
		while play == "yes":
			u = User_Shoot()
			p = CompShoot_strat(u, strat, condition)
			condition = Decide(p)
			#sets condition to 0 or 1 (0 corresponding to a loss and 1 corresponding to a win)
			strat = u
			#sets strat to whichever move the user made in the previous round
			play = str(input("Type \"yes\" to play this mode again,\nor type anything else to return to the main menu: "))
	elif i == "very hard":
		play = "yes"
		while play == "yes":
			Decide(CompShoot_impossible(User_Shoot()))
			play = str(input("Type \"yes\" to play this mode again,\nor type anything else to return to the main menu: "))
			
def main():
	quit = "arbitrary string"
	#Quit must be initially set to anything other than "quit" (fence-post algorithm)
	while quit != "quit":
	#whenever the user types quit, the while loop will end and so will the program.
		choose_mode()
		quit = str(input("Type \"quit\" to quit the game,\nor anything else to continue: "))
		
main()