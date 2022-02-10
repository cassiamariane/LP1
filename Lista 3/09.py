salario = float(input('Digite o valor do salário: '))
if salario <= 2000:
    reajustado = ((salario*0.5) + salario)
    print('Com o reajuste de 50%, o salário aumentou para ', reajustado)
if salario > 2000 and salario <= 5000:
    reajustado = ((salario*0.4) + salario)
    print('Com o reajuste de 40%, o salário aumentou para ', reajustado)
if salario > 5000 and salario <= 7000:
    reajustado = ((salario*0.2) + salario)
    print('Com o reajuste de 20%, o salário aumentou para ', reajustado)
if salario > 7000:
    reajustado = ((salario*0.1) + salario)
    print('Com o reajuste de 10%, o salário aumentou para ', reajustado)