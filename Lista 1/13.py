n = int(input('Digite um número inteiro positivo: '))
limite = []
if n <= 0:
    print('Número inválido.')
else:
    numeros = 1
    while True:
        limite.append(numeros)
        numeros = numeros + 1
        if not numeros <= n:
            break
    print('Os números inteiros de 1 até', n, 'são: ', limite)