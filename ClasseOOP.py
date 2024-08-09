from abc import ABC, abstractmethod

class cliente:
    @abstractmethod
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.__conta = conta
        self.__saldo = saldo

class cliente_fisico(cliente):
    def apresentar(self):
        print(f"Olá! Eu sou: {self.titular}")
        print(f"Minha conta é: {self.conta}") #não vai ser reconhecido pois está como privado
        print("E quero saber meu saldo.")
        return
    
fulano = cliente_fisico("João", "423.050205-21", 25000.00)

fulano.apresentar()

print(f"{fulano.titular}, no momento sua conta possui R$ {fulano.saldo}")  #não vai ser reconhecido pois está como privado