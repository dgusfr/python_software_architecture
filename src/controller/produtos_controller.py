class ProdutosController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def cadastrar_novo_produto(self):
        dados = self.view.obter_dados_produto()

        id_gerado = self.model.salvar_produto(dados["nome"], dados["preco"])

        if id_gerado:
            self.view.exibir_sucesso(id_gerado)
        else:
            self.view.exibir_erro("Falha na persistência")
