from math import sqrt

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('Valor da raiz quadrada: {:.2f}'.format(raiz))
print('Valor da raiz quadrada arredondada para cima: {:.2f}'.format(math.ceil(raiz)))

"""math
ceil = arredondamento pra cima
floor arredondamento para baixo
trunc elimina casas decimais, deixa apens valor inteiro
pow potencia
sqrt raiz quadrada
factorial 

import math traz a biblioteca inter

caso queira apenas uma funcao especifica: from math import ceil ou from math import ceil, sqtr (por exemplo)
"""