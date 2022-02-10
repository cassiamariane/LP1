sexo = input('Digite F para feminino e M para masculino:')
altura = float(input('Digite a altura:'))
if sexo != ('F' and 'M'):
    print('Caractere inválido')
if sexo == 'F':
    peso = (62.1 * altura) - 44.7
if sexo == 'M':
    peso = (72.7 * altura) - 58
print('O peso ideal é:' , round(peso), 'kg')