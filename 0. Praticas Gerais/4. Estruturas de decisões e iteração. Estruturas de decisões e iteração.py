"""
4. Estruturas de decisões e iteração
Implemente um programa que utilize estruturas de decisões (if, else, elif) para determinar se um número inserido pelo usuário é positivo, negativo ou zero. Utilize também loops para pedir novos números até que o usuário insira zero.

Como o programa funciona:

1. O programa define uma função main() que contém um loop infinito (while True).

2. Dentro do loop, ele solicita que o usuário insira um número.

3. O programa usa try e except para capturar exceções, garantindo que o usuário insira um valor numérico válido.

4. Ele verifica se o número é zero e, nesse caso, imprime uma mensagem e sai do loop.

5. Se o número for positivo, imprime que o número é positivo; se for negativo, imprime que é negativo.

6. O loop continua até que o usuário insira zero.
"""

def main():

    while True:

        try:

            numero = int(input('Digite um número inteiro e para encerrar zero: '))

            if numero == 0:
                print('Você digitou ZERO. Saindo do programa')
                break

            elif numero > 0:
                print(f'O {numero} é positivo')
            else:
                print(f'O {numero} é negativo')

        except ValueError:
            print('Por favor, insira um numero valido.')

if __name__ == '__main__':
    main()
