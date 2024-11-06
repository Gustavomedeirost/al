"""
5. Funções e escopos de variáveis
Crie uma função que receba dois números como parâmetros e retorne a soma deles. Em seguida, utilize escopos de variáveis para armazenar o resultado e exibi-lo.
"""

def soma(a, b):
    return a + b

def main():

    try:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))

        resultado = soma(num1, num2)

        print(f' A soma entre {num1} e {num2} é: {resultado}')
    
    except ValueError:
        print('Insira numeros validos!')

if __name__ == '__main__':
    main()