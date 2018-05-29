from random import randint

number = randint(0,99)
guess = int(input("Guess a number between 0 and 99: "))
finished = False
count = 0
while not finished:
	count += 1
	if guess < number:
		guess = int(input("Too low. Guess again: "))
	elif guess > number:
		guess = int(input("Too high. Guess again: "))
	else:
		finished = True
print("Correct. It took you ",count," guesses.")