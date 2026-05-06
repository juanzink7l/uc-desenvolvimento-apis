from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI (title='API de Produtos', version='1.0.0')

# Banco de dados em memória (lista em python)
# em produçao: usariamos SQLlite, PostgreSQL, etc...
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3501.01, "estoque": 10},
    {"id": 2, "nome": "Playstation", "preco": 1459.00, "estoque": 20},
    {"id": 3, "nome": "Iphone", "preco": 7500.00, "estoque": 30}
]
proximo_id = 4 #controlar o proximo id(proximo produto que vier vai ter id = 4)

class ProdutoCreate(BaseModel):
    nome: str
    preço: float
    estoque: int = 0 # pra o estoque ser até 0, nao tem como ter -1 iphones

# GET /produtos -> lista todos os produtos
@app.get('/produtos')
def listar_produtos():
    return produtos 

# GET /produtos/(id -> busca um produto pela id)
@app.get('/produtos/{produto_id}')
def buscar_produto(produto_id: int):
    produto = next(
        (p for p in produtos if p[id] == produto_id),
        None #valor padrao se nao encontrar
    )
    if produto is None:
        return {"erro": f"Produto {produto_id} nao encontrado"}
    return produto

#POST /produtos -> cria um novo produto
@app.post('/produtos', status_code=201)
def criar_produto(produto: ProdutoCreate):
    global proximo_id

    #Cria novo produto com o próximo ID disponivel
    novo_produto = {
        "id": proximo_id,
        "nome": produto.nome, 
        "preco": produto.preco, 
        "estoque": produto.estoque,
    }
    produtos.append(novo_produto)
    proximo_id += 1

    return novo_produto











