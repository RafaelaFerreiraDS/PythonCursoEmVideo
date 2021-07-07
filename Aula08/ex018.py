"""Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse angulo"""
import math

ang = float(input('Digite o valor do ângulo: '))

print('Valor do seno: {:.2f}'.format(math.sin(math.radians(ang))))
print('Valor do cosseno: {:.2f}'.format(math.cos(math.radians(ang))))
print(('Valor da tangente: {:.2f}'.format(math.tan(math.radians(ang)))))
