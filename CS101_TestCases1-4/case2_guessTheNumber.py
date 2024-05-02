# Need to cover the following topics
#   if statements
#   indenting 
#   indented if statements
#   AND/OR

# Number Guesser
import random
start = 1; stop = 10 + 1
correctNumber = random.randrange(start, stop)
print("Hello and welcome to the Number Guesser!\nIf you guess the correct number within 3 guesses then your win!")
print("=========================================================\nPlease make your first guess: ")
#print(correctNumber)
guess         = int(input(""))
round = 1
win = False
if guess < correctNumber:
    print("Sorry, too low!")
elif guess > correctNumber:
    print("Your guess is too high!")
else:
    print("Congratulations, You got it first try!!!")
    quit()
print("=========================================================\nPlease make your second guess: ")
guess         = int(input(""))
if guess < correctNumber:
    print("Sorry, too low!")
elif guess > correctNumber:
    print("Your guess is too high!")
else:
    print("Congratulations, You got it on the second try!!")
    quit()
print("=========================================================\nPlease make your third and final guess: ")
guess         = int(input(""))
if guess < correctNumber:
    print("Sorry, too low! Try again next time!")
elif guess > correctNumber:
    print("Your guess is too high! Try again next time!")
else:
    print("Congratulations, You got it on the last try!")