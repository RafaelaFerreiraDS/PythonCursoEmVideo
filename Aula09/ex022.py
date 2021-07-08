""" Crie um programa que leia o nome completo de uma pessoa e mostre:
    o nome com todas as letrs maiusculas
    o nome com todas as letras minusculas
    quantas letras ao no total, sem considerar espacos
    quantas letras tem o primeiro nome"""

nome = input('Digite o nome completo: ')

print(nome.upper())
print(nome.lower())

nome = nome.split()

print('Letras no primeiro nome: {}'.format(len(nome[0])))

nome = ''.join(nome)

print('Tamanho total sem espaco {}'.format(len(nome)))
