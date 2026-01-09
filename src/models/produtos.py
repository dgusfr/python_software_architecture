from pymongo import MongoClient


class ProdutosModel:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["meu_estoque"]
        self.collection = self.db["produtos"]

    def salvar_produto(self, nome, preco):
        documento = {"nome": nome, "preco": preco}
        resultado = self.collection.insert_one(documento)
        return resultado.inserted_id
