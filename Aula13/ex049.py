num = int(input('Digite um número para qualcular a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))
