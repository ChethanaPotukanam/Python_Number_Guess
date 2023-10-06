#Fun game number guessing using python
import random

low=int(input('Enter low range:'))
high=int(input('Enter high range:'))
val=random.randint(low,high)
print('Guess the number\n\nNOTE:Only 5 chances')
for i in range(0,5):
    guess=int(input('Enter number:'))
    if(guess==val):
        print('YOU WON')
        break
    elif(guess<val):
        print('small number')
    elif(guess>val):
        print('large number')
if(i==4):
    print('You lost')
print("The number is:",val)
