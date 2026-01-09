from src.models.produtos import ProdutosModel
from src.views.produtos_registration import ProdutosRegistrationView
from src.controller.produtos_controller import ProdutosController

model = ProdutosModel()
view = ProdutosRegistrationView()
controller = ProdutosController(model, view)

controller.cadastrar_novo_produto()
