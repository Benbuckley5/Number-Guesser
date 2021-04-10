import random

def guessthenumber():
    pick = random.randint(0,100)
    print(pick)
    while True:
        guess = int(input('pick a number '))
        if guess == pick:
            print('Correct!')
            break
        elif guess < pick:
            print('Too low :(')
        elif guess > pick:
            print('Too high :(')

guessthenumber()
