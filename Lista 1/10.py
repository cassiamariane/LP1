numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
multiplicacao = numero1 * numero2

if numero1 > numero2:
    subtracao = numero1 - numero2
else:
    subtracao = numero2 - numero1
print('O resultado da soma é: ', soma)
print('O resultado da subtração do maior pelo menor é: ', subtracao)
print('O resultado da multiplicação é: ', multiplicacao)

if (numero2 != 0) and (numero1 != 0):
    if numero1 > numero2:
        divisao = numero1/numero2
    if numero1 < numero2:
        divisao = numero2/numero1
    if numero1 == numero2:
        divisao = numero1/numero2
    print('O resultado da divisão do maior pelo menor é: ', divisao)
else: 
    print('Não é possível realizar a divisão, pois o denominador é igual a zero.')
