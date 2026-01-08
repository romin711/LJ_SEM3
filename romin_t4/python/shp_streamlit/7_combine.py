import streamlit as st
from datetime import date
import pandas as pd
st.set_page_config(page_title="Student page",page_icon="🎩",layout="centered")
st.title("🎩 Student Page")
st.header("1. student information")
col1,col2=st.columns(2)
with col1:
    en_no=st.text_input("Enrollment no")
    name=st.text_input("Student Name")
    DOB=st.date_input("Date of Birth")
with col2:
    branch=st.selectbox("Branch",["cse","cst","ce","csit"])
    sem=st.slider("current semester",1,8,1)
st.header("2. Marks Entry")
py=st.number_input("python-1 marks",min_value=0,max_value=100,value=0)
ps=st.number_input("ps marks",min_value=0,max_value=100,value=0)
fsd=st.number_input("fsd marks",min_value=0,max_value=100,value=0)
de=st.number_input("DE marks",min_value=0,max_value=100,value=0)                                 

st.header("3. Feedback")
u=st.slider("How well did you understand subject?",1,10,10)
p=st.radio("class participation",["low","med","high"])
comment=st.text_area("Additional comments")

if st.button("submit record"):
    if not en_no or not name:
        st.error("enter name and enrollment no")
    else:
        df=pd.DataFrame({"enrollment":[en_no],
                         "Name":[name],"Semester":[sem],"branch":[branch],"ps":[ps],"python":[py],"fsd":[fsd],"DE":[de],"Understanding":[u],"participation":[p],"comment":[comment]})
        st.success("Record submitted successfully")
        st.subheader("preview data")
        st.dataframe(df)
        csv=df.to_csv(index=False,encoding="utf-8")
        st.download_button("Download csv file",data=csv,file_name="marks.csv",mime="text/csv")