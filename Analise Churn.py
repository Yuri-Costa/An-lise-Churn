#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# PASSO A PASSO PARA A SOLUÇÃO
# - passo - 1 importar a base de dados
# 
# - passo - 2 visualizar a base de dados(enterder as informções disponivel e decobrir as cagadas das bases de dados)
# 
# - passo - 3 tratamento da base de dados(valores que são numeros e são reconhecidos como letras, valores vazios , etc)
# 
# - passo - 4 Analise inicial: ver como estão os cancelamentos
# 
# - passo - 5 vai olhar cada caracteristica do cliente e ver como aquela caracteristica impacta no cancelamento
# 

# In[2]:


#passo 1
import pandas as pd
tabela = pd.read_csv(r"telecom_users.csv")
#-----------------------------------

#passo 2
display(tabela)
#-----------------------------------


# In[10]:


#PASSO 3
#axis = 1 -> colunas
#axis = 0 -> linhas
#------------------------------------------------------------
#tabela = tabela.drop("Unnamed: 0", axis=1) -> para deletar a coluna
#------------------------------------------------------------

#para mudar de string para float
#tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#------------------------------------------------------------

#para excluir todas as colunas e linhas com todos ou algum os valores vazios any/all
#tabela = tabela.dropna(how="any", axis=0)
#------------------------------------------------------------

print(tabela.info())


# In[14]:


#PASSO 4 
#mostrar os valores contados
display(tabela['Churn'].value_counts())

#em porcentual
display(tabela['Churn'].value_counts(normalize=True))


# In[20]:


import plotly.express as px

#PASSO 5
for coluna in tabela:
    grafico= px.histogram(tabela, coluna, color="Churn" )
    grafico.show()


# In[3]:


#AS CAGADAS
#colunas e linhas vazias
#ver se tem coluna que era pra ser um numero e esta sendo reconhecida como texto
print(tabela.info())


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# - clientes com familias manores, tendem a concelar mais
# 
# - MesesComCliente esta com problema, com muito cancelamento
#     - possivelmente estamos com problema de retenção de clientes nos primeiros meses
#     - ideia: criar programa incentivando o os clientes nos primeiros meses
#     - talvez a capitação de clientes está ruim, talvez estamos com clientes passageiros.
#     - talvez a gente fez alguma promoção maluca no começo, e quando acobou o cliente cancelou
# 
# - clientes de fibra tem muito mais chance de cancelar
#     - provavelmente estamos com algum problema com o serviço de fibra
# 
# - quanto mais serviços o cliente tem menos chance tem de cancelar
#     - temos que criar um programa de incentivo para o cliente contratar mais serviços, nem que tenha que abaixar bastante o preço.
# 
# - contratos mensais tem muito mais chance de cancelar
#     - incentivar contratos de anuais, oferecendo desconto ou outras promoções
# 
#  - forma de pagamento
#      - temos que evitar a opção de pagamento em boleto eletronico
# 
