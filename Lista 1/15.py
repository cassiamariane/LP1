numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
contador = 0
lista = []
if numero1 < numero2:
    contador = numero1
    while contador < (numero2 - 1):
        contador = contador + 1
        lista.append(contador)
else:
    contador = numero2
    while contador < (numero1 - 1):
        contador = contador + 1
        lista.append(contador)
print('Os números entre ', numero1 ,'e', numero2, 'são: ', lista)