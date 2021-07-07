"""Crie um programa que leia um número real qualquer e mostre na tela a sua porçao inteira"""
from math import trunc

num = float(input('Digite um número: '))

print('Parte inteira: {}'.format(trunc(num)))
