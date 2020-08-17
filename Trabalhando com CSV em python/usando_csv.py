import pandas as pd

data = pd.read_csv('train.csv')

#print(data) MOSTRA DADOS

#print(data.head()) # Mostrando apenas o cabeçalho

data_test = pd.read_csv('test.csv') #ATRIBUINDO PLANILHA CSV A VARIAVEL

#print(data_test.tail()) # MOSTRANDO APENAS FINAL DA TABELA

#print(data.info()) #TRAZ TODAS INFORMAÇÕES REDUZIDAS , BOM PARA ANALISAR DESCREPANCIAS
# print(data_test.info())
print(""
      ""
      "")


print('Resumo estatistico')

print(data.describe()) # APRESENTA RESUMO ESTATISTICO

print(data.describe(include='O')) #RESUMO ESTATISTICO CATEGORICO

print('Como renomear colunas')

print(data.columns) # VERIFICA TODAS AS COLUNAS

print(data.rename({'Name': 'Nome', 'Embarked': 'Embarque'}, axis=1, inplace=True)) # RENAME PRA RENOMEAR APOS ISSO NOME ATUAL DA COLUNA E NOME QUAL QUER DAR. AXIS INDICA AONDE SE ENCONTRA


print(data.head(2))

print('Selecionar colunas especificas')

print(data[['Nome','Embarque']]) # DATA SERIES

print('Gerando media , soma ')
print('--------------------------------------')

print('Media', data['Fare'].mean())
print('Soma', data['Survived'].sum())
print('Conta', data['Nome'].count())
print('Mediana', data['Fare'].median())
print('Moda', data['Fare'].mode())
print('Maximo da respectiva coluna', data['Age'].max())
print('Minimo da respeciva coluna', data['Age'].min())

print('Localizando pela iloc que significa que seleciona o id correspondente veja abaixo ')
print('----------------------------------------------------------------------------------')

print(data.iloc[555])#RETORNA ID CORRESPONDENTE
print(data.iloc[[555]]) # retorna em extensoum data frame

print('Pegar e fatiar os dados')
print(data.iloc[1:10])

print('Selecionando com varias condições')
print(data.loc[(data['Age'] >= 3) & (data['Age'] <= 10)]) #VERIFICA ENTRE ESSAS IDADES QUAIS QUE SOBREVIVERAM

print(data.loc[(data['Age'] >= 3) & (data['Age'] <= 10)].mean())

print('Localizar e substituir ')
print('----------------------------------------')

data['Sex'].replace({'male': 'Homem', 'female': 'Mulher'}, inplace=True)# Localiza e modifica
print(data['Sex'])

#print(data['Idade'])
