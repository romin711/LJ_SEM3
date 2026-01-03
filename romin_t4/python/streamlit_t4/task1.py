# wap for streamlit for userinput person name and comment section
import streamlit as st 
st.set_page_config(page_title='hello streamlit' , page_icon='😜' , layout='wide')
name = st.sidebar.text_input('enter name')
comment = st.sidebar.text_area('comment: ')
st.header('your profile')
st.write('profile name: ' , name)
st.write('past comments: ',comment)