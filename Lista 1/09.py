numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
print(numero1, '+', numero2, '=',  soma)
print(numero1, '-', numero2, '=',  subtracao)
print(numero1, '*', numero2, '=',  multiplicacao)
if numero2 != 0:
    divisao = numero1/numero2
    print(numero1, '/', numero2, '=',  divisao)
else:
    print('Não é possível realizar a divisão')