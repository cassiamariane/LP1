def calculo():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = (b**2) - (4*a*c)
    print('O delta vale: ',delta)
    if delta <= 0:
        print('O delta é menor ou igual a zero, as raízes não existem')
    else:
            x1=(-b + delta**0.5)/2*a
            x2=(-b - delta**0.5)/2*a
            print ('As raízes são', round(x1,2), 'e', round(x2,2))
            
calculo()
tecla = input('Digite s para calcular novamente: ')

while (tecla == chr(83)) or (tecla == chr(115)):
    calculo()
    tecla = input('Digite s para calcular novamente: ')