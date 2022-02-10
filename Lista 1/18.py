numeros = 0
resultado = 0
while numeros >= 0:
    resultado = resultado + numeros
    numeros = int(input('Digite números um de cada vez, negativo encerra o loop: '))
print('A soma dos números digitados é: ', resultado)