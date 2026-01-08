import streamlit as st
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="🎁",
    layout="centered"
)
st.title("Welcome to Streamlit")
st.header("This is Header")
st.subheader("This is Subheader")
st.text("This is text")
st.write("***Write here***")
st.markdown('**Bold Text**')
st.markdown('''
            1. Item1
            2. Item2
            3. Sub Item
            ''')
st.markdown("[Open Google](https://www.google.com)")
st.markdown("----")
st.markdown("> This is quote")
st.markdown(''' 
                |Day |Subject |Teacher|
                |----|----    |----   |
                |Mon | Python |  STS  |
                |Tue | FSD    |  MHP  |
            ''' )
st.markdown("![PythonLogo](https://www.python.org/static/community_logos/python-logo.png)")