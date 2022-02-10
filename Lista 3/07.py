binario = []
lista_de_conversoes = []
digitos = int(input('Digite quantos dígitos possui o número binário a ser convertido: '))
for indice in range(digitos):
    binario.append(int(input('Digite os dígitos um de cada vez: ')))
    lista_de_conversoes.append((binario[indice])*2**(digitos-1))
    digitos = digitos - 1
soma = 0 
tamanho = (len(lista_de_conversoes)-1)
for i in range(tamanho):
    soma = soma + lista_de_conversoes[i]
print('O número binário', binario ,'corresponde ao número', soma, 'na base decimal')