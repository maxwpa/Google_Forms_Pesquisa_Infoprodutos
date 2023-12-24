#!/usr/bin/env python
# coding: utf-8

# In[15]:


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import streamlit as st


# In[8]:


df = pd.read_csv('Dados_Tratados.csv')


# In[3]:


#df.columns


# In[13]:


#app = Dash(__name__)

#fig_one = px.bar(df, x="Área mais Consumida", y="Frequência no Consumo", color="Disposição Financeira", barmode="group")

#fig_five = px.pie(df, names="Disposição Financeira", title='Distribuição de Disposição Financeira')

#app.layout = html.Div(children=[
#    html.H1(children='Hello Dash'),
 #   html.Div(children='''Dash: A web application framework for your data.'''),
 #   dcc.Graph(id='one', figure=fig_one),
#    dcc.Graph(id='five', figure=fig_five)
#])

#server = app.server 

#if __name__ == '__main__':
 #   app.run_server(debug=True)


# In[16]:


fig_one = px.bar(df, x="Área mais Consumida", y="Frequência no Consumo", color="Disposição Financeira", barmode="group")
fig_five = px.pie(df, names="Disposição Financeira", title='Distribuição de Disposição Financeira')

st.title('Hello Streamlit')
st.write('Streamlit: Uma estrutura fácil para criação de aplicativos web para seus dados.')

st.plotly_chart(fig_one)
st.plotly_chart(fig_five)


# In[ ]:




