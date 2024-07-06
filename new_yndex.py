from random import randint


number = randint(1, 100)
print('ygadaite chislo ot 1 do 100')

while True:
    guess = int(input('vvedite chislo '))
    if guess < number:
        print('vashe chislo menshe')
    elif guess > number:
        print('vashe chislo bolshe')
    elif guess == number:
        break


print('vi ygadali')


