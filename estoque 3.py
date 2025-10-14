# Vetor inicial de estoque
estoque = [20, 15, 10, 30, 5]

# Função para atualizar o estoque após uma venda
def vender_produto(estoque, indice_produto, quantidade):
    if estoque[indice_produto] >= quantidade:
        estoque[indice_produto] -= quantidade
    else:
        print(f"Estoque insuficiente para o produto {indice_produto + 1}")

# Função para adicionar unidades ao estoque
def adicionar_produto(estoque, indice_produto, quantidade):
    estoque[indice_produto] += quantidade

# Função para exibir o estoque atual (sem usar enumerate)
def exibir_estoque(estoque):
    print("Estoque atual:")
    for i in range(len(estoque)):
        print(f"Produto {i + 1}: {estoque[i]} unidades")

# Atualizações solicitadas:
vender_produto(estoque, 0, 3) # vende 3 unidades do produto 1
vender_produto(estoque, 3, 2) # vende 2 unidades do produto 4
adicionar_produto(estoque, 4, 10) # adiciona 10 unidades ao produto 5

# Exibe o estoque atualizado
exibir_estoque(estoque)
