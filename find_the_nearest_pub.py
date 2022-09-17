import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv('open_pubs.csv')
x = df[['latitude', 'longitude']]
st.title('find the location of 5 nearest pubs')
lat = st.number_input('enter latitude')
long= st.number_input('enter longitude')
submit= st.button(label='submit')
x1 = np.array([lat,long])

dist= np.sqrt(np.sum((x1-x)**2, axis=1))
k=5
sort = np.argpartition(dist,k-1)[:k]
if submit:
    st.map(df.iloc[sort])

