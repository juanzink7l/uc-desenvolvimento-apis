from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI (title='API dos Melhores Filmes', version='1.0.0')

filmes = [
    {"id": 1, "titulo": "As Vantagens de Ser Invisível", "diretor": "Stephen Chbosky", "ano": 2012 , "nota": 10},
    {"id": 2, "titulo": "500 Dias com Ela", "diretor": "Marc Webb", "ano": 2009, "nota": 9.9},
    {"id": 3, "titulo": "Sociedade dos Poetas Mortos", "diretor": "Peter Weir", "ano":1989 , "nota":10}
]

proximo_id = 4

class FilmeCreate(BaseModel):
    titulo: str
    diretor: str
    ano: int
    nota: float

@app.get('/filmes')
def listar_filmes():
    return filmes

@app.get('/filmes/{filme_id}')
def buscar_filme(filme_id: int):
    filme = next(
        (f for f in filmes if f[id] == filme_id),
        None
        )
    if filme is None:
        return {"erro": f"O filme {filme_id} nao foi encontrado!"}
    return filme 

@app.post('/filmes', status_code=201)
def cadastrar_filme(filme: FilmeCreate):
    global proximo_filme
    novo_filme = {
        "id": proximo_id,
        "titulo": filme.titulo, 
        "diretor": filme.diretor, 
        "ano": filme.ano,
        "nota": filme.nota,
    }
    filmes.append(novo_filme)
    proximo_filme += 1

    return novo_filme

















