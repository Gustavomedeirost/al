"""
3. Manipulação de strings
Escreva um programa que receba uma frase do usuário e conte quantas palavras ela possui. Em seguida, inverta a ordem das palavras na frase.
"""

def contar_e_inverter_frase():

    frase = input("Digite uma frase: ")

    palavras = frase.split()

    num_palavras = len(palavras)

    frase_invertida = ' '.join(palavras[::-1])

    print(f"Número de palavras: {num_palavras}")
    print(f"Frase invertida: {frase_invertida}")

# Executar o programa
contar_e_inverter_frase()


