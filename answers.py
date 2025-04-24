from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Usuario, Produto, Pedido, Avaliacao

engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Liste todos os produtos cadastrados no sistema.
def listar_todos_os_produtos():
    produtos = session.query(Produto).all()
    for produto in produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Preço: R${produto.preco}, Categoria: {produto.categoria}, Estoque: {produto.estoque}")
