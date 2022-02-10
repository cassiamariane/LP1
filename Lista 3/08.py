primeiro = [1,2,1,6,8,1]
segundo = [3,4,6,4,5,6]
terceiro = []
print('Conteúdos do primeiro vetor: ', primeiro)
print('Conteúdos do segundo vetor: ', segundo)
for i in range(0, 6):
    terceiro.append(primeiro[i] + segundo[i])
    i = i + 1
print('O resultados das somas dos elementos dos vetores são respectivamente: ', terceiro)