import streamlit as st
import pandas as pd
df=pd.read_csv('open_pubs.csv')
st.title('location of pubs')
select=st.selectbox('select either local authority or postal code',['local_authority', 'postalcode'])
if True:
    if select == 'local_authority':
        form = st.form(key='my_form')
        input = form.text_input('Enter local_authority/postalcode')
        submit = form.form_submit_button(label='submit')
        lat = df.loc[df['local_authority'] == input, 'latitude']
        long = df.loc[df['local_authority'] == input, 'longitude']
        rdf = pd.DataFrame((lat,long))
        st.map(rdf)
    elif select == 'postalcode':
        form = st.form(key = 'my_form')
        input = form.text_input('Enter local_authority/postalcode')
        submit = form.form_submit_button(label='submit')
        lat = df.loc[df['local_authority'] == input, 'latitude']
        long = df.loc[df['local_authority'] == input, 'longitude']
        rdf = pd.DataFrame((lat, long))
        st.map(rdf)





