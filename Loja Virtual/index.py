from users.clientes import Cliente;
from users.gerencia import Gerencia;

login = input("Digite se você é cliente ou gerente: ")
nome = input("Digite seu nome: ")
if login.lower() == "cliente":
    print(f'Olá cliente {nome.upper()}, Bem Vindo a loja virtual!')
    nome = Cliente(nome)
    nome.produtosDisponiveisParaVenda()
    nome._Addproduto()
    nome._itensDoCarrinho()
    nome._removerProduto()
    nome._subtotalDoCarrinho()

elif login.lower() == "gerente":
    print(f'Olá gerente {nome.upper()}, Bem Vindo a loja virtual!')
    nome = Gerencia(nome)
    nome._adicionarProdutoNoEstoque()
    nome.produtosDisponiveisParaVenda()
    nome._removerProdutoDoEstoque()
