class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print(f"Não há produtos cadastrados na loja {self.nome}.")
        else:
            print(f"Produtos da loja {self.nome}:")
            for produto in self.produtos:
                print(f"- {produto.nome}, Preço: R${produto.preco:.2f}")

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco