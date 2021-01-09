class Conta:
    # Construtor da classe
    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Função que gera o extrato bancário de uma conta
    def extrato(self):
        print("****** EXTRATO BANCÁRIO ******")
        print(f'Número da Conta: {self.numero}')
        print(f'Titular da Conta: {self.titular}')
        print(f'Saldo da Conta: {self.saldo}')
        print("******************************")

    # Função para depositar um valor em uma conta
    def deposita(self, valor):
        self.saldo += valor

    # Função para sacar o valor de uma conta
    def saca(self, valor):
        self.saldo -= valor