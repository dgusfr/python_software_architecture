class ProdutosRegistrationView:
    def obter_dados_produto(self):
        print("--- CADASTRO DE PRODUTOS ---")
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")

        dados = {"nome": nome, "preco": preco}
        return dados

    def exibir_sucesso(self, id_produto):
        print(f"Sucesso! Produto cadastrado com o ID: {id_produto}")

    def exibir_erro(self, mensagem):
        print(f"Erro ao cadastrar: {mensagem}")
