#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from replit import clear
from art import logo

def check_answer(_guess_number, _secret_number,_attemps):
	if _guess_number > _secret_number:
		print("To high")
		return _attemps - 1
	if _guess_number < _secret_number:
		print("To low")
		return _attemps -1
	else:
		print("Match")
	
def game():
	
	print(logo)
	
	difficult = input("Do you want to play 'easy' or 'hard' level? ")	
	if difficult == "easy":
		attempts = 10
		print(f"You are select 'easy' mode. Yo have {attempts} attempts")
	else:
		attempts = 5
		print(f"You are in 'Hard' mode. You haver {attempts} attempts")
	
	secret_number = random.randrange(1,100)
	guess_number = 0
	while not guess_number == secret_number and attempts > 0:
		guess_number = int(input("Guess number: "))

		attempts = check_answer(guess_number, secret_number, attempts)
		print(f"You have {attempts} left")
		if attempts == 0:
			print("You lose!!")
			return

	other_play = input("Do you want to play another play? 'y' or 'no'") 
	if other_play == "y":
		clear()
		game()

game()
		
	

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

