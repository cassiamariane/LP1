quantidade = int(input('Quantas maçãs foram compradas?'))
if quantidade < 12:
    valor =  quantidade* 0.45
if quantidade >= 12:
    valor = quantidade* 0.36
print('O valor total é de: R$', round(valor, 2))