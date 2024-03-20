operacao = int()
while (operacao) != 5:
    print(f'1:SOMA\n2:SUBTRAÇÃO\n3:MULTIPLICAÇÃO\n4:DIVISÃO\n5:SAIR')
    operacao = int(input('Escolha a operação matemática: '))
    if operacao == 1:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: ')) 
        print(f'\nO resultado da operação é:\n {num1} + {num2} = {num1 + num2}\n\n')
    elif operacao == 2:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: ')) 
        print(f'\nO resultado da operação é:\n {num1} - {num2} = {num1 - num2}\n\n')
    elif operacao == 3:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: ')) 
        print(f'\nO resultado da operação é:\n {num1} * {num2} = {num1 * num2}\n\n')
    elif operacao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um segundo número: ')) 
        print(f'\nO resultado da operação é:\n {num1} / {num2} = {num1 / num2}\n\n')
    elif operacao > 5:
        print('\nEscolha uma das opções validas\n')
    elif operacao == 5:
        print('Você saiu da calculadora')
        break