import streamlit as st
c=st.selectbox("select course",["python","DE","FSD","PS"])
lect=st.multiselect("days",["mon","tues","wed","thus","Fri","sat"])
lect_no=st.radio("lect no",[1,2,3,4])
st.write("course",c,(",".join(lect) if lect else "None"))