from random import randrange

num = randrange (1, 101)

trial = 1
guess = int(input ('Guess a number: '))
prevdiff = abs (guess - num)
if guess < 1 or guess > 100:
    print ('OUT OF BOUNDS')
elif prevdiff == 0:
    pass
elif prevdiff > 10:
    print ('COLD')
else:
    print ('WARM')

while prevdiff != 0:
    guess = int(input ('Guess another number: '))
    trial += 1
    if guess < 1 or guess > 100:
        print ('OUT OF BOUNDS')
        continue
    diff = abs (guess - num)
    if diff < prevdiff:
        print ('WARMER')
    else:
        print ('COLDER')
    prevdiff = diff

print (f'Correct Guess! No. of trials: {trial}')