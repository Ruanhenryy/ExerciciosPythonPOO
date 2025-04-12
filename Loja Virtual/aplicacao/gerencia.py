from aplicacao.produtos import Produtos;

class Gerencia(Produtos):
    def __init__(self):
        super().__init__()

    def __adicionarProdutoNoEstoque(self, removerProduto, valor):
        if not self.produtosDisponiveis:
            self.produtosDisponiveis[removerProduto] = valor
            print(f'{removerProduto} já foi adicionado!')
            return
        if removerProduto in self.produtosDisponiveis:
            self.produtosDisponiveis[removerProduto] = valor
            print(f'{removerProduto} já foi adicionado!')
            return
        print(f'Produto adicionado!')
        self.produtosDisponiveis[removerProduto] = valor

    def __removerProdutoDoEstoque(self, removerProduto):
        if not self.produtosDisponiveis:
            print(f'{removerProduto} não tem produtos no estoque!')
            return
        if removerProduto in self.produtosDisponiveis:
            self.produtosDisponiveis.pop(removerProduto)
            print(f'{removerProduto} foi removido do estoque!')
            return
        print(f'Produto não encontrado no estoque!')
