import streamlit as st
st.set_page_config(page_title="hello streamlit",page_icon="@",layout="centered")
st.title("welcome to streamlt")
st.header("this is header")
st.subheader("this is subheader")
st.text(" This is text")
st.write("this is **_write()_** ")
st.markdown(" <h3 style='color:red';>this is _markdown_ </h3>",unsafe_allow_html=True)
code="""
def add(a,b):
    return a+b
sum=add(3,5)
print(sum)
"""
st.code(code,language="python")
st.code(code,language="C")

n1=st.number_input("enter no1:")
n2=st.number_input("enter no2:")
a=st.selectbox("operation",["add","sub"])
if a=="add":
    st.write("addition:",n1+n2) 
if a=="sub":
    st.write("subtraction:",n1-n2) 