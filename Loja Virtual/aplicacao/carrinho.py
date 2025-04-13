from aplicacao.estoque import Produtos;

class Carrinho(Produtos):
    def __init__(self):
        super().__init__()
        self.__itensCarrinho = []
        self.__quantidadeDeItensNoCarrinho = 0
        self.__subTotal = 0.0
    
    def adicionarProdutoNoCarrinho(self):
        addProduto = input("Digite o nome do produto a ser adicionado: ")
        if addProduto in self.__itensCarrinho:
            print(f'{addProduto} já está no carrinho')
            return
        
        print(f'Produto adicionado no carrinho!')
        self.__itensCarrinho.append(addProduto.lower())

    def removerProdutoDoCarrinho(self):
        removerProduto = input("Digite o nome do produto a ser removido: ")
        if not self.__itensCarrinho:
            print("Carrinho vazio!")
            return
        elif removerProduto in self.__itensCarrinho:
            print(f'{removerProduto} foi removido do carrinho!')
            self.__itensCarrinho.remove(removerProduto.lower())
            return
        
        print(f'{removerProduto} não está no carrinho!')
    
    def itensDoCarrinho(self):
        print('Itens adicionados ao carrinho⬇️')
        for item in self.__itensCarrinho:
            print(item)

    def valorDaCompra(self):
        for item in self.__itensCarrinho:
            if item in self.produtosDisponiveis:
                self.__subTotal += self.produtosDisponiveis.get(item)
            else:
                print(f'{item} não está disponivel!')
        print(f'O subtotal do carrinho é de R$ {self.__subTotal}!')