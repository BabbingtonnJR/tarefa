num1 = float(input('Digite um número: '))
num2 = float(input('Digite um segundo número: '))

print(f'1:SOMA \n 2:SUBTRAÇÃO \n 3:MULTIPLICAÇÃO \n 4:DIVISÃO \n 5:SAIR')

operacao = int(input('Escolha a operação matemática: '))

if operacao == 1:
    print(f'O resultado da operação é:\n {num1} + {num2} = {num1 + num2}')
elif operacao == 2:
    print(f'O resultado da operação é:\n {num1} - {num2} = {num1 - num2}')
elif operacao == 3:
    print(f'O resultado da operação é:\n {num1} x {num2} = {num1 * num2}')
elif operacao == 4:
    print(f'O resultado da operação é:\n {num1} / {num2} = {num1 / num2}')
elif operacao == 5:
    print(f'Você saiu da calculadora')
else:
    print(f'Comando inválido')