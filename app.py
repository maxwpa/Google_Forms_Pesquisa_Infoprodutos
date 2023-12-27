import streamlit as st

st.set_page_config(page_title='DashBoard')

link = st.text_input('Insira o link aqui:')

st.write('Link inserido:', link)

