import streamlit as st 
st.set_page_config(page_title='hello streamlit' , page_icon='😜' , layout='centered')
st.title('welcome to streamlit')
st.header('this is header')
st.subheader('this is subheader')
st.text('this is text')
st.write('this is **_write()_** ')
st.markdown('<h3 style="color:red";> this is _markdown_ </h3>',unsafe_allow_html=True)

code = """
def add(a,b):
    return a+b
sun = add(2,5)
print(sum)
"""

st.code(code,language='python')
st.code(code,language='C')