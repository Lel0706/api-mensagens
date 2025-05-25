from app import ma
from marshmallow import fields


class MensagemSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    conteudo = fields.Str(required=True)


mensagem_schema = MensagemSchema()
mensagens_schema = MensagemSchema(many=True)
