from aplicacao.loja import Loja;

class Cliente(Loja):
    def __init__(self, nomeCliente):
        super().__init__()
        self.__nomeCliente = nomeCliente
        self.produtosFavoritos = []
    def _favoritar(self):
        produtoFavorito = input(str("Digite o nome do produto que deseja favoritar: "))
        if produtoFavorito in self.produtosFavoritos:
            print(f'Olá {self.__nomeCliente}, {produtoFavorito} Já está na lista de favoritos!')
            return
        print(f'Olá {self.__nomeCliente}, {produtoFavorito} foi adicionado a sua lista de favoritos!')
        self.produtosFavoritos.append(produtoFavorito)
    
    def _Addproduto(self):
        self._carrinho.adicionarProdutoNoCarrinho()

    def _removerProduto(self):
        self._carrinho.removerProdutoDoCarrinho()

    def _itensDoCarrinho(self):
        self._carrinho.itensDoCarrinho()

    def _subtotalDoCarrinho(self):
        self._carrinho.valorDaCompra()