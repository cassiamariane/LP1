km1 = int(input('Digite a marcação de Km no início do dia: '))
km2 = int(input('Digite a marcação de Km no fim do dia: '))
gastol = int(input('Quantos litros de gasolina foram gastos hoje? '))
vt = int(input('Quanto no total em R$ você recebeu hoje? '))
media = (km2 - km1)/gastol
gastoabs = gastol*2.75
lucro = vt - gastoabs
print('A media de consumo de hoje foi de: ', media)
print('O gasto com abastecimento de hoje foi de: R$ ', round(gastoabs, 2))
print('O lucro de hoje foi de: R$ ', round(lucro, 2))