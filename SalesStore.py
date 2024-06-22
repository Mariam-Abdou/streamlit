
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv('Sales_Store_Preprocessed.csv')
st.title('Sales Store Analysis')

totSales = df['Sales'].sum().round(2)
profit = df['Profit'].sum().round(2)

c1, c2 = st.columns(2)
with c1:
    st.metric('Total Sales', totSales)
with c2:
    st.metric('Profit', profit)

st.header('Profit over Years')
fig1 = px.pie(df, 'Year', 'Profit', color_discrete_sequence=px.colors.qualitative.Alphabet_r)
st.plotly_chart(fig1)

st.header('Profit')
fig2 = ff.create_distplot( [df['Profit']], ['Profit'], show_hist=False )
st.plotly_chart(fig2)
