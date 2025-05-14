from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Produto, Pedido, Avaliacao
from datetime import datetime

engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

produtos_caros = session.query(Produto).filter(Produto.valor_estoque > 1000).all()

for produto in produtos_caros:
    print(f"{produto.nome} - Valor em estoque: R${produto.valor_estoque}")


print(Produto.valor_estoque) 