import streamlit as st 
st.set_page_config(page_title='hello streamlit' , page_icon='😜' , layout='wide')
st.title('Student profile')
st.sidebar.header('profile setting')
student = st.sidebar.text_input('student name', 'IRK')
branch = st.sidebar.selectbox('branch',["ce" , "csit" , "cst" , "cse"])
sem = st.sidebar.slider("semester",1,8,1)
st.markdown('.......')
col1,col2 = st.columns([1,2])
with col1: 
    st.write('student information')
    st.write(f" student name: **{student}** ")
    st.write('branch: ',branch)
    st.write('semester: ',sem)

with col2:
    st.subheader('about')
    st.write('this is about student')

with st.expander('subjects'):
    st.write('PS')
    st.write('FSD')
    st.write('PYTHON')
    st.write('DE')
    