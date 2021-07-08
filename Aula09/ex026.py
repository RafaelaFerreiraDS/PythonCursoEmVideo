frase = input('Digite uma frase: ').upper()

print('A letra "A" apareceu {} vezes.'.format(frase.count('A')))

print('A primeira letra "A" aparece na posição:', frase.find('A') + 1)

print('A última letra "A" aparece na posição:', frase.rfind('A') + 1)
