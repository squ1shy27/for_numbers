from random import randint


number = randint(1, 100)
print('ygadaite chislo ot 1 do 100')

while True:
    guess = int(input('vvedite chislo'))
    if guess < number:
        print('vashe chislo menshe')
    if guess > number:
        print('vashe chislo bolshe')
    if guess == number:
        break


print('vi ygadali')


