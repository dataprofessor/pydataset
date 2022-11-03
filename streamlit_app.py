import streamlit as st
import pandas as pd
from pydataset import data

st.title('🎈 pydataset')

selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)
#data()[data()['dataset_id'] == selected_data]['title']
dataset = data()[ data()['dataset_id'] == selected_data]

st.write(dataset)


#st.header('Datasets')
#st.subheader('List of dataset')
#with st.expander('Show list of dataset'):
#    st.write(data())

#st.subheader(f'Selected data (`{selected_data}`)')
#st.write(data(selected_data))
