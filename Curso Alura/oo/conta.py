class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo o objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        disponivel = (self.__saldo + self.__limite)
        return valor <= disponivel

    def saca (self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print ("Saldo Insuficiente")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return (self.__titular)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,novo_limite):
        self.__limite = novo_limite

    @staticmethod  ## é da classe, não precisa criar um objeto prara acessar este método
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB" : "001", "Itaú" :"341", "Caixa":"104", "Bradesco": "237"}
