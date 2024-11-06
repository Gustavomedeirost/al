"""
8. Orientação a Objetos – Herança e polimorfismo
Explore herança e polimorfismo criando classes que representam diferentes animais. 
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

    def emitir_som(self):
        raise NotImplementedError("Este metedo deve ser implementado pelas subclasses.")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au Au")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau")