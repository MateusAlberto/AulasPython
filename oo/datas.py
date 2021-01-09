class Data:
    # Construtor da classe Data
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Imprime a data formatada no padrão brasileiro
    def formatada(self):
        print("{:02d}/{:02d}/{:04d}".format(self.dia, self.mes, self.ano))