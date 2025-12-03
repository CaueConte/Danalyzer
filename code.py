import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
pd.options.display.max_rows = 9999

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
#reorganizando datas fromatadas erradas

df.drop_duplicates(inplace=True)
#Removendo dados duplicados

# print(df.isnull()) #verifica o que tem de
# print(df)
# new_df = df.dropna(inplace=True)
# print(new_df)
# print(f'----\n{df}')
#removendo linhas com valores nulos

#'df.method({col: value}, inplace=True)' or 
#df[col] = df[col].method(value)
df.fillna({'InvoiceID': 'nao informado'}, inplace=True)
# df.fillna({'Date': 'nao informado'}, inplace=True)
df.fillna({'City': 'nao informado'}, inplace=True)
df.fillna({'Category': 'nao informado'}, inplace=True)
df.fillna({'Product': 'nao informado'}, inplace=True)
# df.fillna({'UnitPrice': 'nao informado'}, inplace=True)
# df.fillna({'Quantity': 'nao informado'}, inplace=True)
# df.fillna({'Total': 'nao informado'}, inplace=True)
df.fillna({'PaymentMethod': 'nao informado'}, inplace=True)
df.fillna({'CustomerGender': 'nao informado'}, inplace=True)
# print(df)
#sugestao:armazenar dados que nao podem ser calculados de colunas ao inves de excluir
#nao foram feitos parametros para trocar nomes de colunas de numeros para nao ocasionar
#erro nos calculos e amostragens

for x in df.index:
    if pd.isna(df.loc[x, 'Total']) and df.loc[x, 'UnitPrice']!=None and df.loc[x, 'Quantity']!=None:
        y = df.loc[x, 'UnitPrice']* df.loc[x, 'Quantity']
        df.loc[x, 'Total'] = y
#fazendo valores 'Total', os quais estão nulos, serem calculados com base no preço e quantidade
for x in df.index:
    if pd.isna(df.loc[x, 'UnitPrice']) and df.loc[x, 'Quantity']!=None and df.loc[x, 'Total']!=None:
        y = df.loc[x, 'Total']/df.loc[x, 'Quantity']
        df.loc[x, 'UnitPrice'] = y
#calculando preco da unidade onde eram nulos com abse no total e quantidade
for x in df.index:
    if pd.isna(df.loc[x, 'Quantity']) and df.loc[x, 'Total']!=None and df.loc[x, 'UnitPrice']!=None:
        y = df.loc[x, 'Total']/df.loc[x, 'UnitPrice']
        df.loc[x, 'Quantity'] = y
#calculando quantidade onde era nulo com base no total e preco sda unidade


# print(df)

# df.dropna(inplace=True) #remvoendo rows com nulo em qualquer coluna
# df['UnitPrice'] = df['UnitPrice'].astype(float)
# df['Quantity'] = df['Quantity'].astype(int)
# df['Total'] = df['Total'].astype(float)
#forçando variaveis para um tipo especifico

# for x in df.index:
#     if df.loc[x, "City"]=='Três ':
#         df.loc[x, "City"] = 'Três Lagoas' #forma de consertar valores errados
print(df)

df['City'] = df['City'].replace('Três ', 'Três Lagoas')#corrigindo valor errado em city

print(df.groupby('City')['Total'].sum())#somando valor total de cada cidade
print(' ')
print(df.groupby('City')['Quantity'].sum())#soma total de produtos vendidos

vendas = df.groupby('Product')['Quantity'].sum()
maisVendido = vendas.idxmax()
quantidade = vendas.max()
print(f'Mais vendido: {maisVendido} Quantidade: {quantidade}')
#produto mais vendido

vendas2 = df.groupby(['City', 'Product'])['Quantity'].sum()
maisVendido2 = vendas2.groupby(level=0).idxmax()
print(maisVendido2)
#maisvendido por cidade

#plot
g =df.groupby('City')['Total'].sum()
plt.bar(g.index, g.values)
plt.xlabel('Cidade')
plt.ylabel('Total de vendas')
plt.title('Total de vendas de cada cidade')
plt.show()
#mostrando o total de produtos vendidos por cidade

#fazer grafico de produtos e quantidade de cada
plt.bar(vendas.index, vendas.values)
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.title('Quantidade de produtos vendidos')
plt.xticks(rotation=85)
plt.show()

#consertar indices reptidos, 60 e 59 ou 50 alguma coisa
