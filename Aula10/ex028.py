import random

num = int(input('Adivinhe o número: '))

x = random.randint(0, 5)
if num == x:
    print('Acertou! O número certo é {}.'.format(x))
else:
    print('Errou! O número certo é {}.'.format(x))
