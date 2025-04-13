class Produtos:
    def __init__(self):
        self.produtosDisponiveis = {
            "manga":10,
            "camisa":21.99,
            "short":15.99
        }
    
    def listaDeProdutosEValores(Self):
        print("Produtos e seus valores:")
        for produto in Self.produtosDisponiveis:
            contador = 1
            print(f'{contador} -> {produto} R${Self.produtosDisponiveis.get(produto)}')
            contador += 1