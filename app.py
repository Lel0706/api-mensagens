from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
class Mensagem(BaseModel):
    id: int
    conteudo: str
mensagens: List[Mensagem] = []
@app.post("/mensagens", response_model=Mensagem)
def criar_mensagem(mensagem: Mensagem):
    mensagem.id = len(mensagens) + 1  
    mensagens.append(mensagem)
    return mensagem
@app.get("/mensagens", response_model=List[Mensagem])
def listar_mensagens():
    return mensagens
@app.get("/mensagens/{id}", response_model=Mensagem)
def obter_mensagem(id: int):
    for m in mensagens:
        if m.id == id:
            return m
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")

@app.put("/mensagens/{id}", response_model=Mensagem)
def atualizar_mensagem(id: int, mensagem: Mensagem):
    for m in mensagens:
        if m.id == id:
            m.conteudo = mensagem.conteudo
            return m
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")
@app.delete("/mensagens/{id}")
def deletar_mensagem(id: int):
    for m in mensagens:
        if m.id == id:
            mensagens.remove(m)
            return {"mensagem": "Deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Mensagem não encontrada")
