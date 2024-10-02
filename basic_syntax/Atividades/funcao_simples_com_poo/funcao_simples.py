# 1. **Implemente uma função** que receba dois números e retorne a soma deles.
class Numeros:
    soma = 0;
    n1 = 0;
    n2 = 0;

    #def __init__(self, n1, n2):
        #self.n1 = n1  # Atributo da instância
        #self.n2 = n2  # Atributo da instância

    def receber_numeros(self): 
        self.n1 = input("Escreva o primeiro numero: ") 
        self.n2 = input("Escreva o segundo numero: ")

    def soma(self):
        self.soma = int(self.n1) + int(self.n2)

    def print_this(self):
        print('soma: ', self.soma)

def main():
    numero = Numeros()

    numero.receber_numeros()
    numero.soma()
    numero.print_this()

main()