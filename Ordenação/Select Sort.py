lista = [12, 7, 2, 20]

print(lista)
tamanhoDaLista = len(lista)
for indice in range(tamanhoDaLista-1):
    menorIndice = indice
    for indice2 in range(indice, tamanhoDaLista):
        if lista[indice2] < lista[menorIndice]:
            menorIndice = indice2
            if lista[indice] > lista[menorIndice]:
                auxiliar = lista[indice]
                lista[indice] = lista[menorIndice]
                lista[menorIndice] = auxiliar
print(lista)