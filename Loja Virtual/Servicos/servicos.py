from abc import ABC, abstractmethod;

@abstractmethod
class Servicos(ABC):
    def __init__(self):
        pass
    def mostrarProdutos(self):
        print("Produtos disponíveis em estoque: ")
        pass