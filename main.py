from user import Usuario
from store import Loja, Produto

class Sistema:
    def __init__(self):
        self.lojas = []
        self.usuarios = []

    def cadastrar_loja(self, nome, endereco):
        loja = Loja(nome, endereco)
        self.lojas.append(loja)
        print(f"Loja '{nome}' cadastrada com sucesso.")

    def cadastrar_produto_na_loja(self, nome_loja, nome_produto, preco):
        loja = self.encontrar_loja(nome_loja)
        if loja:
            produto = Produto(nome_produto, preco)
            loja.adicionar_produto(produto)
            print(f"Produto '{nome_produto}' adicionado à loja '{nome_loja}'.")

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def listar_lojas(self):
        if not self.lojas:
            print("Não há lojas cadastradas.")
        else:
            print("Lojas cadastradas:")
            for loja in self.lojas:
                print(f"- {loja.nome}, Endereço: {loja.endereco}")
                
    def listar_usuarios(self):
        if not self.usuarios:
            print("Não há usuários cadastrados.")
        else:
            print("Usuários cadastrados:")
            for usuario in self.usuarios:
                print(f"- {usuario.nome}, Email: {usuario.email}")
                
    def encontrar_loja(self, nome_loja):
        for loja in self.lojas:
            if loja.nome == nome_loja:
                return loja
        print(f"Loja '{nome_loja}' não encontrada.")
        return None

def menu():
    sistema = Sistema()

    while True:
        print("\n---- Menu ----")
        print("1. Cadastrar Loja")
        print("2. Cadastrar Produto na Loja")
        print("3. Cadastrar Usuário")
        print("4. Listar Lojas")
        print("5. Listar Usuários")
        print("6. Listar Produtos de uma Loja")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_loja = input("Nome da loja: ")
            endereco = input("Endereço da loja: ")
            sistema.cadastrar_loja(nome_loja, endereco)

        elif opcao == "2":
            nome_loja = input("Nome da loja onde deseja adicionar o produto: ")
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            sistema.cadastrar_produto_na_loja(nome_loja, nome_produto, preco)

        elif opcao == "3":
            nome_usuario = input("Nome do usuário: ")
            email_usuario = input("Email do usuário: ")
            sistema.cadastrar_usuario(nome_usuario, email_usuario)

        elif opcao == "4":
            sistema.listar_lojas()

        elif opcao == "5":
            sistema.listar_usuarios()

        elif opcao == "6":
            nome_loja = input("Digite o nome da loja para listar os produtos: ")
            loja = sistema.encontrar_loja(nome_loja)
            if loja:
                loja.listar_produtos()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()