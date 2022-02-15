lista = [36, 8, 1, 9]
print(lista)
tamanhoDaLista = len(lista)
contador = 0
while contador < tamanhoDaLista:
    for indice in range(tamanhoDaLista-1):
        if lista[indice + 1] < lista[indice]:
            auxiliar = lista[indice]
            lista[indice] = lista[indice + 1]
            lista[indice + 1] = auxiliar
            contador = contador + 1
print(lista)