from fastapi import FastAPI

app = FastAPI(
    title = "Minha primeira API",
    description="Criada no Senai por: Juan Pablo com FastAPI",
    version="1.0.0"
)
""" GET / informaçoes sobre a API """
@app.get('/sobre')
def raiz(): 
    return {
        "api": "Minha primeira API",
        "versão": "1.0.0",
        "framework": "FastAPI",
        "linguagem": "Python 3",
        "escola": "Senai"
    }

@app.get('/saudacao/{nome}')
def saudar(nome: str):
    return {
        "mensagem": f"Eai, {nome}! Navegue em nossa API",
        "nome_recebido": nome
    }