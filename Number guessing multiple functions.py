import random

def Rand():
    n = random.randint(0,100)
    return n

def guessthenumber(pick):
    while True:
        guess = int(input('Pick a number '))
        if guess == pick:
            print('Correct!')
            break
        elif guess < pick:
            print('Too low :(')
        elif guess > pick:
            print('Too high :(')

guessthenumber(Rand())