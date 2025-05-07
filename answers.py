from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, Produto, Pedido, Avaliacao
from datetime import datetime

# Configuração da sessão
engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Função: all()
# 1. Liste todos os produtos cadastrados no sistema.
# produtos = session.query(Produto).all()
# print("Produtos cadastrados:")
# for produto in produtos:
#     print(produto.nome)

# 2. Recupere todos os usuários ativos com mais de 18 anos.
# usuarios_ativos = session.query(Usuario).filter(Usuario.ativo == True, Usuario.idade > 18).all()
# print("\nUsuários ativos com mais de 18 anos:")
# for usuario in usuarios_ativos:
#     print(usuario.nome)

# # 3. Obtenha todos os pedidos feitos depois de 01/03/2025 com quantidade superior a 5.
# pedidos_filtro = session.query(Pedido).filter(Pedido.data_pedido > datetime(2025, 3, 1), Pedido.quantidade > 5).all()
# print("\nPedidos feitos depois de 01/03/2025 com quantidade > 5:")
# for pedido in pedidos_filtro:
#     print(f"Pedido ID: {pedido.id}, Quantidade: {pedido.quantidade}")

# Função: first()
# 4. Encontre o primeiro usuário cadastrado no sistema.
# usuario_primeiro = session.query(Usuario).first()
# print("\nPrimeiro usuário cadastrado:", usuario_primeiro.nome)

# 5. Verifique qual é o produto mais barato da categoria "eletrônicos".
# produto_barato = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco).first()
# print("\nProduto mais barato da categoria 'eletrônicos':", produto_barato.nome)

# 6. Determine o último pedido realizado por qualquer usuário.
# ultimo_pedido = session.query(Pedido).order_by(Pedido.data_pedido.desc()).first()
# print("\nÚltimo pedido realizado:", ultimo_pedido.id)

# Função: get(pk)
# 7. Recupere os dados completos do usuário com ID 7.
# usuario_7 = session.query(Usuario).get(7)
# print("\nDados do usuário com ID 7:", usuario_7.nome, usuario_7.email)

# 8. Verifique se existe um produto com ID 5 e estoque positivo.
# produto_estoque = session.query(Produto).get(5)
# existe_produto = produto_estoque and produto_estoque.estoque > 0
# print("\nProduto com ID 5 e estoque positivo:", existe_produto)

# 9. Obtenha o pedido de ID 3 junto com os dados do usuário associado.
# pedido_3 = session.query(Pedido).filter(Pedido.id == 3).join(Usuario).first()
# print("\nPedido ID 3 com dados do usuário associado:", pedido_3.usuario.nome)

# Função: filter()
# 10. Encontre usuários com idade entre 25 e 35 anos.
# usuarios_25_35 = session.query(Usuario).filter(Usuario.idade.between(25, 35)).all()
# print("\nUsuários com idade entre 25 e 35 anos:")
# for usuario in usuarios_25_35:
#     print(usuario.nome)

# 11. Liste pedidos com status "cancelado" ou "pendente" feitos depois de 2024.
# pedidos_status = session.query(Pedido).filter(Pedido.status.in_(['cancelado', 'pendente']), Pedido.data_pedido > datetime(2024, 1, 1)).all()
# print("\nPedidos com status 'cancelado' ou 'pendente' feitos depois de 2024:")
# for pedido in pedidos_status:
#     print(pedido.id, pedido.status)

# 12. Selecione produtos com preço acima de R$ 500 que tiveram pelo menos 1 pedido.
# produtos_filtrados = session.query(Produto).filter(Produto.preco > 500).join(Pedido).group_by(Produto.id).having(func.count(Pedido.id) > 0).all()
# print("\nProdutos com preço acima de R$ 500 e com pelo menos 1 pedido:")
# for produto in produtos_filtrados:
#     print(produto.nome)

# Função: filter_by()
# 13. Busque todos os usuários com status inativo.
# usuarios_inativos = session.query(Usuario).filter_by(ativo=False).all()
# print("\nUsuários inativos:")
# for usuario in usuarios_inativos:
#     print(usuario.nome)

# 14. Encontre produtos da categoria "livros" com preço inferior a R$ 100.
# produtos_livros = session.query(Produto).filter_by(categoria='livros').filter(Produto.preco < 100).all()
# print("\nProdutos da categoria 'livros' com preço inferior a R$ 100:")
# for produto in produtos_livros:
#     print(produto.nome)

# 15. Obtenha os 3 produtos mais caros com estoque disponível.
# produtos_caros = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco.desc()).limit(3).all()
# print("\n3 produtos mais caros com estoque disponível:")
# for produto in produtos_caros:
#     print(produto.nome)

# Função: order_by()
# 16. Liste todos os usuários em ordem alfabética de nome.
# usuarios_ordenados = session.query(Usuario).order_by(Usuario.nome).all()
# print("\nUsuários em ordem alfabética:")
# for usuario in usuarios_ordenados:
#     print(usuario.nome)

# 17. Ordene os produtos do mais caro para o mais barato.
# produtos_ordenados = session.query(Produto).order_by(Produto.preco.desc()).all()
# print("\nProdutos do mais caro para o mais barato:")
# for produto in produtos_ordenados:
#     print(produto.nome)

# 18. Organize os pedidos por data de criação (mais recentes primeiro) e depois por status.
# pedidos_ordenados = session.query(Pedido).order_by(Pedido.data_pedido.desc(), Pedido.status).all()
# print("\nPedidos ordenados por data e status:")
# for pedido in pedidos_ordenados:
#     print(f"Pedido ID: {pedido.id}, Data: {pedido.data_pedido}, Status: {pedido.status}")

# Função: limit(n)
# 19. Liste os 10 primeiros usuários cadastrados no sistema.
# usuarios_limitados = session.query(Usuario).limit(10).all()
# print("\n10 primeiros usuários cadastrados:")
# for usuario in usuarios_limitados:
#     print(usuario.nome)

# 20. Obtenha os 5 produtos mais baratos disponíveis no estoque.
# produtos_limitados = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco).limit(5).all()
# print("\n5 produtos mais baratos disponíveis no estoque:")
# for produto in produtos_limitados:
#     print(produto.nome)

# 21. Selecione os 3 pedidos mais recentes feitos por usuários com idade maior que 30 anos.
# pedidos_recentes = session.query(Pedido).join(Usuario).filter(Usuario.idade > 30).order_by(Pedido.data_pedido.desc()).limit(3).all()
# print("\n3 pedidos mais recentes feitos por usuários com idade maior que 30 anos:")
# for pedido in pedidos_recentes:
#     print(f"Pedido ID: {pedido.id}, Data: {pedido.data_pedido}")

# Função: offset(n)
# 22. Liste os usuários cadastrados, ignorando os 5 primeiros resultados.
# usuarios_offset = session.query(Usuario).offset(5).all()
# print("\nUsuários cadastrados, ignorando os 5 primeiros:")
# for usuario in usuarios_offset:
#     print(usuario.nome)

# 23. Obtenha os produtos mais caros, pulando os 3 primeiros resultados na ordenação por preço.
# produtos_offset = session.query(Produto).order_by(Produto.preco.desc()).offset(3).all()
# print("\nProdutos mais caros, pulando os 3 primeiros resultados:")
# for produto in produtos_offset:
#     print(produto.nome)

# 24. Liste os pedidos realizados, ignorando os 8 primeiros, mas ordenados pela data de criação de forma decrescente.
# pedidos_offset = session.query(Pedido).order_by(Pedido.data_pedido.desc()).offset(8).all()
# print("\nPedidos realizados, ignorando os 8 primeiros:")
# for pedido in pedidos_offset:
#     print(f"Pedido ID: {pedido.id}, Data: {pedido.data_pedido}")

# Função: count()
# 25. Conte quantos usuários estão cadastrados no sistema.
# total_usuarios = session.query(Usuario).count()
# print("\nTotal de usuários cadastrados:", total_usuarios)

# 26. Determine o número de pedidos realizados com status 'entregue'.
# total_pedidos_entregue = session.query(Pedido).filter(Pedido.status == 'entregue').count()
# print("\nNúmero de pedidos 'entregue':", total_pedidos_entregue)

# 27. Conte quantos produtos existem na categoria 'eletrônicos' com estoque maior que 0 e preço acima de R$ 100,00.
# total_produtos_eletronicos = session.query(Produto).filter(Produto.categoria == 'eletrônicos', Produto.estoque > 0, Produto.preco > 100).count()
# print("\nNúmero de produtos na categoria 'eletrônicos' com estoque > 0 e preço > R$ 100:", total_produtos_eletronicos)

# Função: distinct()
# 28. Liste todas as categorias únicas de produtos disponíveis no sistema.
# categorias_unicas = session.query(Produto.categoria).distinct().all()
# print("\nCategorias únicas de produtos:")
# for categoria in categorias_unicas:
#     print(categoria[0])

# 29. Identifique as idades únicas dos usuários cadastrados no banco de dados.
# idades_unicas = session.query(Usuario.idade).distinct().all()
# print("\nIdades únicas dos usuários:")
# for idade in idades_unicas:
#     print(idade[0])

# 30. Obtenha todos os status únicos dos pedidos realizados por usuários ativos com mais de 25 anos de idade.
# status_unicos = session.query(Pedido.status).join(Usuario).filter(Usuario.ativo == True, Usuario.idade > 25).distinct().all()
# print("\nStatus únicos de pedidos realizados por usuários ativos com mais de 25 anos:")
# for status in status_unicos:
#     print(status[0])

# Função: join()
# 31. Liste o nome dos usuários e os IDs dos pedidos que eles realizaram.
# usuarios_pedidos = session.query(Usuario.nome, Pedido.id).join(Pedido).all()
# print("\nUsuários e IDs dos pedidos realizados:")
# for usuario, pedido_id in usuarios_pedidos:
#     print(usuario, pedido_id)

# 32. Obtenha o nome dos produtos e a quantidade comprada em cada pedido realizado por um usuário específico chamado 'João'.
# pedidos_joao = session.query(Produto.nome, Pedido.quantidade).join(Pedido).join(Usuario).filter(Usuario.nome == 'João').all()
# print("\nProdutos e quantidades compradas por João:")
# for nome, quantidade in pedidos_joao:
#     print(nome, quantidade)

# 33. Liste todos os usuários que fizeram pedidos de produtos da categoria "livros", incluindo o nome do produto e a quantidade comprada em cada pedido.
# usuarios_livros = session.query(Usuario.nome, Produto.nome, Pedido.quantidade).\
#     join(Pedido, Pedido.usuario_id == Usuario.id).\
#     join(Produto, Produto.id == Pedido.produto_id).\
#     filter(Produto.categoria == 'livros').all()
# print("\nUsuários que fizeram pedidos de produtos da categoria 'livros':")
# for nome_usuario, nome_produto, quantidade in usuarios_livros:
#     print(nome_usuario, nome_produto, quantidade)

# Função: exists()
# 34. Verifique se existe algum usuário chamado "Maria" cadastrado no sistema.
# existe_maria = session.query(Usuario).filter(Usuario.nome == 'Maria').exists()
# print("\nExiste algum usuário chamado Maria?", session.query(existe_maria).scalar())

# 35. Confirme se há algum pedido realizado para um produto com estoque igual a 0.
# existe_pedido_estoque_zero = session.query(Pedido).join(Produto).filter(Produto.estoque == 0).exists()
# print("\nExiste algum pedido para um produto com estoque igual a 0?", session.query(existe_pedido_estoque_zero).scalar())

# 36. Determine se existe algum pedido feito por um usuário inativo com status 'pendente'.
# existe_pedido_inativo_pendente = session.query(Pedido).join(Usuario).filter(Usuario.ativo == False, Pedido.status == 'pendente').exists()
# print("\nExiste algum pedido feito por um usuário inativo com status 'pendente'?", session.query(existe_pedido_inativo_pendente).scalar())

# Função: add_columns()
# 37. Retorne o nome e a idade de todos os usuários cadastrados no sistema.
# usuarios_nome_idade = session.query(Usuario.nome, Usuario.idade).all()
# print("\nNome e idade de todos os usuários cadastrados:")
# for nome, idade in usuarios_nome_idade:
#     print(nome, idade)

# 38. Liste o nome dos produtos e seus preços para todos os itens cadastrados no banco de dados.
# produtos_nome_preco = session.query(Produto.nome, Produto.preco).all()
# print("\nNome e preço de todos os produtos cadastrados:")
# for nome, preco in produtos_nome_preco:
#     print(nome, preco)

# 39. Obtenha o nome dos usuários, o ID dos pedidos e a quantidade comprada em cada pedido realizado por eles.
# usuarios_pedidos_quantidade = session.query(Usuario.nome, Pedido.id, Pedido.quantidade).join(Pedido).all()
# print("\nUsuários, IDs dos pedidos e quantidades compradas:")
# for usuario, pedido_id, quantidade in usuarios_pedidos_quantidade:
#     print(usuario, pedido_id, quantidade)

# Função: group_by()
# 40. Agrupe os pedidos pelo status e conte quantos pedidos existem para cada status diferente no banco de dados.
# pedidos_status_count = session.query(Pedido.status, func.count(Pedido.id)).group_by(Pedido.status).all()
# print("\nPedidos agrupados pelo status:")
# for status, count in pedidos_status_count:
#     print(status, count)

# 41. Agrupe os produtos pela categoria e calcule o preço médio dos produtos em cada categoria disponível no sistema.
# produtos_categoria_preco_medio = session.query(Produto.categoria, func.avg(Produto.preco)).group_by(Produto.categoria).all()
# print("\nPreço médio dos produtos por categoria:")
# for categoria, preco_medio in produtos_categoria_preco_medio:
#     print(categoria, preco_medio)

# 42. Agrupe os pedidos por usuário e calcule a soma total das quantidades compradas por cada usuário ativo com mais de 30 anos de idade.
# pedidos_usuario_quantidade_total = session.query(Usuario.nome, func.sum(Pedido.quantidade)).join(Pedido).filter(Usuario.idade > 30, Usuario.ativo == True).group_by(Usuario.id).all()
# print("\nSoma total das quantidades compradas por cada usuário ativo com mais de 30 anos:")
# for usuario, total_quantidade in pedidos_usuario_quantidade_total:
#     print(usuario, total_quantidade)

# Função: having()
# 43. Agrupe os pedidos pelo status e filtre apenas aqueles com mais de 3 registros em um único status usando having().
# pedidos_status_filtro = session.query(Pedido.status, func.count(Pedido.id)).group_by(Pedido.status).having(func.count(Pedido.id) > 3).all()
# print("\nPedidos agrupados pelo status com mais de 3 registros:")
# for status, count in pedidos_status_filtro:
#     print(status, count)

# 44. Agrupe os produtos pela categoria e filtre as categorias cujo preço médio seja maior que R$ 200,00 utilizando having().
# produtos_categoria_preco_filtro = session.query(Produto.categoria, func.avg(Produto.preco)).group_by(Produto.categoria).having(func.avg(Produto.preco) > 200).all()
# print("\nCategorias com preço médio maior que R$ 200,00:")
# for categoria, preco_medio in produtos_categoria_preco_filtro:
#     print(categoria, preco_medio)

# 45. Agrupe os pedidos por usuário, calcule a soma total das quantidades compradas e filtre apenas aqueles usuários cuja soma total seja maior que 10 usando having().
# pedidos_usuario_quantidade_filtro = session.query(Usuario.nome, func.sum(Pedido.quantidade)).join(Pedido).group_by(Usuario.id).having(func.sum(Pedido.quantidade) > 10).all()
# print("\nUsuários com soma total das quantidades compradas maior que 10:")
# for usuario, total_quantidade in pedidos_usuario_quantidade_filtro:
#     print(usuario, total_quantidade)