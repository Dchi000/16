import random
secretNumber=random.randint(1,20)
print('i am thinking of a number between 1 and 20.')
for guessessTaken in range(1,7):
    print('take a guess.')
    guess=int(input())
    if guess<secretNumber:
        print('your guess is too low.')
    elif guess>secretNumber:
        print('your guess is too hight.')
    else:
        break
if guess==secretNumber:
    print('Good job! you gussed my number in '+str(guessesTaken)+'guesses!')
else:
    print('Nope.The number I was thinking of was'+str(secretNumber))
