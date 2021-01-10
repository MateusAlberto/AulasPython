class Conta:
    # Construtor da classe
    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Gets e sets
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Função que gera o extrato bancário de uma conta
    def extrato(self):
        print("****** EXTRATO BANCÁRIO ******")
        print(f'Número da Conta: {self.__numero}')
        print(f'Titular da Conta: {self.__titular}')
        print(f'Saldo da Conta: {self.__saldo}')
        print("******************************")

    # Função para depositar um valor em uma conta
    def deposita(self, valor):
        self.__saldo += valor

    # Função para sacar o valor de uma conta
    def saca(self, valor):
        self.__saldo -= valor

    # Função para realizar uma transferência
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
