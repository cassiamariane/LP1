numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
lista = []
if numero1 < numero2:
    contador = numero1
    while contador <= numero2:
        lista.append(contador)
        contador = contador + 1
else:
    contador = numero2
    while contador <= numero1:
        lista.append(contador)
        contador = contador + 1
print(lista)