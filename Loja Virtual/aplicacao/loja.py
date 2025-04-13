from aplicacao.estoque import Produtos;
from aplicacao.carrinho import Carrinho;

class Loja:
    def __init__(self):
        self._estoque = Produtos()
        self._carrinho = Carrinho()

    def produtosDisponiveisParaVenda(self):
        self._estoque.listaDeProdutosEValores()