#passo 1 = importar banco de dados

#passo 2 = calcular o faturamento de cada loja

#passo 3 = calcular a quantidade de produtos vendidos de cada loja

#passo 4 = calcular o ticket médio de cada loja


# Passo 1
import pandas as pd
tabela_vendas = pd.read_excel("Vendas.xlsx")
display(tabela_vendas)

# Passo 2
tabela_faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()   # agrupar por ID Loja e fazer a soma do valor final
tabela_faturamento = tabela_faturamento.sort_values(by = "ID Loja", ascending= True) # a função sort_value vai ordenar em ordem alfabética ascendente (ascending = True)
display(tabela_faturamento)

# Passo 3
tabela_quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()  # groupby("nome da coluna") em sql group by, vai definir o indice para "ID Loja"
display(tabela_quantidade)

# Passo 4
ticket_medio = (tabela_faturamento['Valor Final'] / tabela_quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:"Ticket Medio"}) # trocar nome da coluna '0' para Ticket Medio
display(ticket_medio)

