import streamlit as st
st.set_page_config(page_title="hello streamlit",page_icon="@",layout="wide")
st.title("Student Profile")
st.sidebar.header("Profile setting")
student=st.sidebar.text_input("student name","Swati Patel")
branch=st.sidebar.selectbox("Branch",["ce","csit","cst","cse"])
sem=st.sidebar.slider("semester",1,8,1)
st.sidebar.markdown("........")
col1,col2=st.columns([1,2])
with col1:
    st.write("Student information")
    st.write(f" student name: **{student}** ")
    st.write("Branch: ",branch)
    st.write("semester: ",sem)
with col2:
    st.subheader("About")
    st.write("this is about student")
with st.expander("subjects"):
    st.write("PS")
    st.write("FSD")
    st.write("Python")
    st.write("DE")