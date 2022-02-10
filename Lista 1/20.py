nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 6:
    print(nome, 'Aprovado, com média', round(media, 2))
else:
    print(nome, 'Reprovado, com média', round(media, 2))