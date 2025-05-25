from flask import request
from flask_restful import Resource
from app.models.mensagem_model import mensagem_schema, mensagens_schema


mensagens = []
proximo_id = 1

class MensagensResource(Resource):
    def get(self):
        return mensagens_schema.dump(mensagens), 200

    def post(self):
        global proximo_id
        erros = mensagem_schema.validate(request.json)
        if erros:
            return erros, 400

        nova_mensagem = {
            "id": proximo_id,
            "conteudo": request.json["conteudo"]
        }
        mensagens.append(nova_mensagem)
        proximo_id += 1

        return mensagem_schema.dump(nova_mensagem), 201

class MensagemResource(Resource):
    def get(self, id):
        mensagem = next((m for m in mensagens if m["id"] == id), None)
        if mensagem:
            return mensagem_schema.dump(mensagem), 200
        return {"erro": "Mensagem não encontrada"}, 404

    def put(self, id):
        erros = mensagem_schema.validate(request.json)
        if erros:
            return erros, 400

        for mensagem in mensagens:
            if mensagem["id"] == id:
                mensagem["conteudo"] = request.json["conteudo"]
                return mensagem_schema.dump(mensagem), 200

        return {"erro": "Mensagem não encontrada"}, 404

    def delete(self, id):
        for mensagem in mensagens:
            if mensagem["id"] == id:
                mensagens.remove(mensagem)
                return {"mensagem": "Deletada com sucesso"}, 200

        return {"erro": "Mensagem não encontrada"}, 404
