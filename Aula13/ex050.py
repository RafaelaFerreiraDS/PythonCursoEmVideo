soma = 0
for c in range(0, 6):
    num = float(input('Digite um número: '))
    if num % 2 == 0:
        soma += num

print('Soma dos números pares: {}'.format(soma))
