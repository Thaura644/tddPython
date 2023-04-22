import random
#beginner program guessing game

guessesTaken = 0

print("Hello! What is your name?")
myName = input()

number = random.randint(1,20)
print("Well," + myName + " i am thinking of anumber between 1 and 20.")

for guessesTaken in range(6):
	print("Take a guess. ") 
	guess = input()
	guess = int(guess)

	if guess < number:
		print('your guess is too low')
	
	if guess > number:
		print('your guess is too high')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Good job, '+myName+'! You guessed my number in '+ guessesTaken + ' guesses!' )
if guess != number:
	number = str(number)
	print('Nope. The number i was thinking of was ' +  number + '.')

