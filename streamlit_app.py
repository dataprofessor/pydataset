import streamlit as st
import pandas as pd
from pydataset import data

st.title('🎈 pydataset')

selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)
title_data = data()[ data()['dataset_id'] == selected_data]['title']

st.header('Datasets')
st.subheader('List of dataset')
with st.expander('Show list of dataset'):
    st.write(data())

st.subheader(f'Selected data (`{selected_data}`)')
st.info(title_data)
st.write(data(selected_data))
