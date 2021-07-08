frase = 'Curso em Video Python'

print('impriminto intervalo: {}'.format(frase[9:13]))

print('impriminto intervalo: {}'.format(frase[9:21]))  # imprime intervalo

print('impriminto intervalo: {}'.format(frase[9:21:2]))  # imprime intervalo pulando de 2 em 2

print('impriminto intervalo: {}'.format(frase[:13]))  # comeca do inicio e vai até o indice indicado

print('impriminto intervalo: {}'.format(frase[9:]))  # comeca no indice indicado e vai até o fim da string

print('impriminto intervalo: {}'.format(frase[9::3]))  # comeca no indice indicado, vai até o fim e salta de 3 em 3

print('tamanho da string {}'.format(len(frase)))

print('quantas letras "o" aparece na frase:', frase.count('o'))  # 'o' minusculo

print('quantas letras "o" aparece na frase:', frase.count('o', 0, 13))  # considera a contagem até o indice 12,
# sempre pega um valor menor

print('encontra inicia a sequencia de caracter:', frase.find('deo'))  # rfind analisa de tras pra frente

print(frase.find('android'))  # quando a sequencia de strings nao contem na frase, informa -1

print('Curso' in frase)  # informa se contem a sequencia na string

print(frase.replace('Python', 'Android'))  # altera a sequencia de string por outra

print(frase.upper())  # caixa alta

print(frase.lower())  # caixa baixa

print(frase.capitalize())  # apenas primeira letra maiuscula

print(frase.title())  # deixa todas as palavras com a primeira letra maiuscula

frase = '   Aprendendo Python   '

print(frase)

print(frase.strip())  # retira os espacos desnecessarios nas extremidades

print(frase.rstrip())  # trata/retira apenas os espacos da extremidade direita

print(frase.lstrip())  # trata/retira apenas os espacos da extremidade esquerda

frase = 'Curso em Video Python'

frase = frase.split()  # gera uma lista

print(frase)

frase = '-'.join(frase)  # junta as palavras da lista usando '-' como separador, se colocar ' ' fica espaco

print(frase)
