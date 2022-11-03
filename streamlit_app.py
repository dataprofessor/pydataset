import streamlit as st
from pydataset import data

st.title('🎈 pydataset')

selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)

st.header('Datasets')
st.subheader('List of dataset')
with st.expander('Show list of dataset'):
    st.write(data())

st.subheader(f'Selected data (`{selected_data}`)')
st.write(str(selected_data.title))
st.write(data(selected_data))
