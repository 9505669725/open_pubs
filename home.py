import streamlit as st
import pandas as pd
import io
st.title('welcome to open pubs')
st.write('over view of the open pub dataset')
df1=pd.read_csv('open_pubs.csv')

df=st.dataframe(df1)
st.write('the columns of the dataset are')
st.write(df1.columns)
st.write('the shape of dataset is:{}'.format(df1.shape))
st.text('')

st.write('the description of dataset is')
st.dataframe(df1.describe())

buffer=io.StringIO()
df1.info(buf=buffer)
s=buffer.getvalue()
st.write('the info of dataset is')
st.text(s)
st.text('')
st.write('the bar plot')
st.bar_chart(df1['local_authority'].value_counts().head(20))