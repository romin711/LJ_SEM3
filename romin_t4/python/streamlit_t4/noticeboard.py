import streamlit as st 
from datetime import date

st.set_page_config(page_title=' notice board' , layout='wide')
st.title('notice board')
st.sidebar.header('filter notice')
selected = st.sidebar.selectbox('notice category ', ['all' , 'exam' , 'workshop' , 'internship' , 'general'])
show_past = st.sidebar.checkbox('show past notices ', value=True)
notices = [
    {
        'title' : 't4 exam schedule',
        'category' : 'exam',
        'date' : date(2026,2,1)
    },

    {
        'title' : 't3 exam schedule',
        'category' : 'exam',
        'date' : date(2025,12,12)
    },

    {
        'title' : 't4 exam schedule',
        'category' : 'workshop',
        'date' : date(2026,2,11)
    },

    {
        'title' : 'internship schedule',
        'category' : 'internship',
        'date' : date(2026,2,2)
    },

    {
        'title' : 'PTM',
        'category' : 'general',
        'date' : date(2026,2,21)
    }
]

st.header('notices')
st.subheader('filter applied')
st.write(f' category **{selected}** ')
st.write('include past notices',show_past)

for i in notices:
    if selected != 'all' and i['category'] != selected:
        continue
    with st.expander(f'{i['title']} --- {(i['category'])}'):
        st.write('date',i['date'])
        st.write('notice details')


        