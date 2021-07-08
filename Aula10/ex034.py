salario = float(input('digite o valor do salário: '))

if salario >= 1250:
    print('O aumento é R${:.2f}. Totalizando salario: R$ {:.2f}'.format(salario * 0.1, salario * 1.1))
else:
    print('O aumento é R${:.2f}. Totalizando salario: R$ {:.2f}'.format(salario * 0.15, salario * 1.15))
