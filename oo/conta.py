class Conta:
    # Construtor da classe
    def __init__(self, numero, titular, saldo = 0.0, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Gets e sets
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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

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

    # Função que verifica se um determinado valor pode ser sacado
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    # Função para sacar o valor de uma conta
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    # Função para realizar uma transferência
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
