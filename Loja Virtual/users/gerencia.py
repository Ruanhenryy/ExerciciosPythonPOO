from aplicacao.loja import Loja;

class Gerencia(Loja):
    def __init__(self, nomeGerente):
        super().__init__()
        self.__nomeGerente = nomeGerente

    def _adicionarProdutoNoEstoque(self):
        adicionarProduto = input("Digite o nome do produto a seu adicionado: ")
        valor = float(input("Digite o valor do produto: "))
        if adicionarProduto in self._estoque.produtosDisponiveis:
            print(f'{adicionarProduto} já foi adicionado!')
            return
        print(f'Produto adicionado!')
        self._estoque.produtosDisponiveis[adicionarProduto.lower()] = valor

    def _removerProdutoDoEstoque(self):
        removerProduto = input("Digite o nome do produto a ser removido: ")
        if removerProduto.lower() in self._estoque.produtosDisponiveis:
            self._estoque.produtosDisponiveis.pop(removerProduto.lower())
            print(f'{removerProduto} foi removido do estoque!')
            return
        print(f'{removerProduto} não encontrado no estoque!')