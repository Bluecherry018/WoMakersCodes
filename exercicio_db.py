# Alexandra Floriano

import sqlite3

conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Amanda",22,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Fernando",18,"Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Leticia",23,"Biologia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"José",19,"Farmácia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Valquiria",20,"Matemática")')

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecionar todos os registros da tabela "alunos".
dados_alunos = cursor.execute('SELECT * FROM alunos')
for dados in dados_alunos:
    print(dados)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados_alunos_20 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for dados in dados_alunos_20:
    print(dados)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados_alunos_Eng = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY curso DESC')
for dados in dados_alunos_Eng:
    print(dados)

# d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) FROM alunos ')
print(cursor.fetchone()[0])

# Sem utilizar COUNT()
# total = cursor.execute('SELECT * FROM alunos')
#
# count = 0
#
# for n_total in total:
#     count += 1
# print(count)

# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade="19" WHERE nome="Amanda"')

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 1')

# 5. Criar uma Tabela e Inserir Dados

#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1,"Osvaldo", 35, 5000.40)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2,"Giovana", 26, 2020.80)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3,"Melissa", 22, 300.60)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4,"Carlos", 55, 27000.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5,"Antônio", 47, 4560.90)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6,"Carmem", 62, 12340.20)')

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
clientes_30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

for clientes in clientes_30:
    print(clientes)

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes')
print(cursor.fetchone()[0])


# c) Encontre o cliente com o saldo máximo.
cliente_max = cursor.execute('SELECT nome FROM clientes ORDER BY saldo LIMIT 1')
for cliente in cliente_max:
    print(cliente)

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
print(cursor.fetchone()[0])

# outra forma de fazer, sem usar COUNT()
# acima_100 = cursor.execute('SELECT * FROM clientes WHERE saldo > 1000')
#
# count = 0
#
# for acima in acima_100:
#     count += 1
# print(count)

# 7. Atualização e Remoção com Condições

# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo=2000 WHERE nome="Osvaldo"')

# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=2')

# 8. Junção de Tabelas

# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id a tabela "clientes"), produto (texto) e valor (real).
cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor REAL, PRIMARY KEY(id), FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1,"Manteiga", 25.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2,2,"Arroz", 27.50)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3,3,"Feijão", 7.40)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4,4,"Detergente", 3.12)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(5,5,"Banana", 6.20)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
consulta = cursor.execute('SELECT nome,produto ,valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id')

for pessoa in consulta:
    print(pessoa)

conexao.commit()
conexao.close