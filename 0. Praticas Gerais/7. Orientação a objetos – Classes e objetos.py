"""
Orientação a objetos – Classes e objetos
Crie uma classe que represente um carro, com atributos como modelo, cor e ano. Instancie objetos dessa classe e exiba suas características.
"""

def main():

    class Carro:
        def __init__(self, modelo, cor, ano):
            self.modelo = modelo
            self.cor = cor
            self.ano = ano
        
        def exibir_caracteristica(self):
            print(f'Modelo: {self.modelo}')
            print(f'Cor: {self.cor}')
            print(f'Ano: {self.ano}')
            
    #Instancias dos objetos da classe carro    
    Car1 = Carro('Bronco', 'Preto', '2023')
    Car2 = Carro('Sonic', 'Vermelho', '2017')
    Car3 = Carro('Fusca', 'Branco', '1970')

    Car1.exibir_caracteristica()
    Car2.exibir_caracteristica()
    Car3.exibir_caracteristica()
    
if __name__ == '__main__':
    main()