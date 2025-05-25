from app import api
from app.controllers.mensagem_controller import MensagensResource, MensagemResource


api.add_resource(MensagensResource, "/mensagens")
api.add_resource(MensagemResource, "/mensagens/<int:id>")
