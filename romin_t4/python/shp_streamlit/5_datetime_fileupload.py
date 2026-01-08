from datetime import date ,time
import streamlit as st
st.title(" Date ,Time, FILE upload")
exam_date=st.date_input("select date",value=date.today())
start_time=st.time_input("select time",value=time(14,0))
file=st.file_uploader("upload your pdf  file",type=["pdf"])
st.write("exam start date and time",exam_date,start_time)

