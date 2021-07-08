print('Crescente')
for c in range(1, 11):  # (a, b, c) a: inicio, b: fim, c: decremento/incremento
    print(c)

print('\nDecrescente')
for c in range(10, 0, -1):
    print(c)

n = int(input('Digite um número: '))

for c in range(0, n, 2):
    print(c)
