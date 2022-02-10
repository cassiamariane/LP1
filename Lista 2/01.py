numero = int(input('Digite um número para o cálculo do fatorial: '))
contador = 1
fatorial = 1
if numero < 0:
    print('Não existe fatorial de número negativo')
else:
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1
        if contador > numero:
            print('O fatorial de ', numero, 'é igual a ', fatorial)