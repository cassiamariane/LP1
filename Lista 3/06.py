listaDeConversoes = []
binario = []
decimal = int(input('Que número você quer converter para binário? '))
while decimal > 0:
    resto = decimal%2
    listaDeConversoes.append(resto)
    decimal = decimal//2
tamanho = len(listaDeConversoes) - 1
for j in range(tamanho, -1,-1):
    binario.append(listaDeConversoes[j])
    j = j - 1
    
print(binario)