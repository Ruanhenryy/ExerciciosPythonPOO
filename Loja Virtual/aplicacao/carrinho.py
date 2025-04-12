from aplicacao.produtos import Produtos;

class Carrinho(Produtos):
    def __init__(self):
        super().__init__()
        self.itensCarrinho = []
        self.quantidadeDeItensNoCarrinho = 0
        self.subTotal = 0.0
    
    def _adicionarProdutoNoCarrinho(self):
        addProduto = input("Digite o nome do produto a ser adicionado: ")
        if addProduto in self.itensCarrinho:
            print(f'{addProduto} já está no carrinho')
            return
        
        print(f'Produto adicionado no carrinho!')
        self.itensCarrinho.append(addProduto.lower())

    def _removerProdutoDoCarrinho(self):
        removerProduto = input("Digite o nome do produto a ser removido: ")
        if not self.itensCarrinho:
            print("Carrinho vazio!")
            return
        elif removerProduto in self.itensCarrinho:
            print(f'{removerProduto} foi removido do carrinho!')
            self.itensCarrinho.remove(removerProduto.lower())
            return
        
        print(f'{removerProduto} não está no carrinho!')
    
    def _itensDoCarrinho(self):
        print('Itens adicionados ao carrinho⬇️')
        for item in self.itensCarrinho:
            print(item)

    def _valorDaCompra(self):
        for item in self.itensCarrinho:
            if item in self.produtosDisponiveis:
                self.subTotal += self.produtosDisponiveis.get(item)
            else:
                print(f'{item} não está disponivel!')
        print(f'O valor da compra foi de R$ {self.subTotal}!')