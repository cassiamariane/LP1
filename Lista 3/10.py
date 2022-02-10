total = int(input('Digite a quantidade total de tudo o que foi pedido: '))
tdspedidos = []

for indice in range(total, 1, -1):
    codigo = int(input('Digite o código do produto: '))
    if codigo != 100 and codigo != 101 and codigo != 102 and codigo != 103:
        print('Código de produto inválido.')
        break
    quantidade = int(input('Digite a quantidade adquirida desse produto: '))
    if codigo == 100:
        valor = 4.5*quantidade
        print('Você comprou', quantidade, 'Misto quente(s), no valor de R$', valor)
        tdspedidos.append(valor)
    if codigo == 101:
        valor = 5.0*quantidade
        print('Você comprou', quantidade, 'Refrigerante(s), no valor de R$', valor)
        tdspedidos.append(valor)
    if codigo == 102:
        valor = 2.0*quantidade;
        print('Você comprou', quantidade, 'Pão(es) de queijo, no valor de R$', valor)
        tdspedidos.append(valor)
    if codigo == 103:
        valor = 6.0*quantidade;
        print('Você comprou', quantidade, 'Suco(s), no valor de R$', valor)
        tdspedidos.append(valor)
    if quantidade == total:
        break
    
soma = 0
for i in range(0,len(tdspedidos),1):
    soma = soma + tdspedidos[i]
print('O valor total a ser pago é R$ ', soma)