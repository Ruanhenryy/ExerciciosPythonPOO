from Servicos.servicos import Servicos;

class Produtos(Servicos):
    def __init__(self):
        self.produtosDisponiveis = {
            "camisa":21.99,
            "short":15.99
        }
    
    def mostrarProdutos(self):
        super().mostrarProdutos()
        for produto in self.produtosDisponiveis:
            print(produto)