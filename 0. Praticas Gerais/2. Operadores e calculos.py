"""
2. Operadores e cálculos
Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.
"""

def calculo():
    print('Escolha a opção da operação:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

Operacao = input('Escolha a operação: ')

num1 = float(input('numero1: '))
num2 = float(input('numero2: '))

if Operacao == '1':
    print(f'{num1} + {num2} = {num1 + num2}')
elif Operacao == '2':
    print(f'{num1} - {num2} = {num1 - num2}')
elif Operacao == '3':
    print(f'{num1} * {num2} = {num1 + num2}')
elif Operacao == '4':
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Não é possivel realizar a operação com 0.')
else:
    print('Operação invalida')
