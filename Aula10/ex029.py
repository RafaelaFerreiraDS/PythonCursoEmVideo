velocidade = float(input('Digite a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado. A multa vai custar R${:.2f}'.format(multa))
else:
    print('Não foi multado.')