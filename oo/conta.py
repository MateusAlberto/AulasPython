class Conta:
    #Construtor da classe
    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite