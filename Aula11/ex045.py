from random import randint

escolha = input('Escolha entre pedra, papel ou tesoura: ').upper()

if escolha == 'PAPEL':
    escolha = 0
elif escolha == 'PEDRA':
    escolha = 1
elif escolha == 'TESOURA':
    escolha = 2
else:
    print('Escolha inválida...')

palavras = ('pedra', 'papel', 'tesoura')

x = randint(0, 2)

print('Computador escolheu {}.'.format(palavras[x]))

if escolha - x == -1 or escolha - x == 2:
    print('Você ganhou!')
elif escolha == x:
    print('Empatou')
else:
    print('Você perdeu :(')
