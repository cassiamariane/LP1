numero = int(input('Digite um número de 1 a 10: '))
multiplicador = 0
while multiplicador <= 9:
    resultado = numero * multiplicador
    print(numero, 'X', multiplicador, '=', resultado)
    multiplicador = multiplicador + 1