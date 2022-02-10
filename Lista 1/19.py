lista = []
numeros = int(input('Digite números um por vez, negativo encerra o loop: '))
while numeros >= 0:
    lista.append(numeros)
    numeros = int(input('Digite números um por vez, negativo encerra o loop: '))
tamanho = len(lista)    
for indice in range(tamanho-1):
    menorIndice = indice
    for indice2 in range(indice, tamanho):
        if lista[indice2] < lista[menorIndice]:
            menorIndice = indice2
            if lista[indice] > lista[menorIndice]:
                auxiliar = lista[indice]
                lista[indice] = lista[menorIndice]
                lista[menorIndice] = auxiliar
print('O menor número digitado foi: ', lista[0], 'e o maior número digitado foi: ', lista[tamanho-1])