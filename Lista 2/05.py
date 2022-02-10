largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
caixas = round((area/1.5)*4)
print('Para cobrir todas as paredes da cozinha, serão necessárias', caixas, 'caixas de azulejo')