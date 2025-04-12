from aplicacao.carrinho import Carrinho;

class Loja(Carrinho):
    def __init__(self):
        super().__init__()
        self.produtosFavoritos = []

    def favoritar(self):
        produtoFavorito = input(str("Digite o nome do produto que deseja favoritar: "))
        if produtoFavorito in self.produtosFavoritos:
            print(f'{produtoFavorito} Já está na lista de favoritos!')
            return
        print(f'{produtoFavorito} foi adicionado a lista de favoritos!')
        self.produtosFavoritos.append(produtoFavorito)
    