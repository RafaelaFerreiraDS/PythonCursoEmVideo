"""Faça um programa que leia o comprimento do cateto oposto  e do cateto adjacente de um
triangulo retangulo, calcule e mostre o comprimento da hipotenusa"""
from math import sqrt, pow

c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))

h = sqrt(pow(c1, 2) + pow(c2, 2))

print('Tamanho da hipotenusa: {:.2f}'.format(h))
