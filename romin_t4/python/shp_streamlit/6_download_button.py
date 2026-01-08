import streamlit as st
import pandas as pd
if st.button("click to generate marksheet"):
    df=pd.DataFrame({"Roll_No":[1,2,3,4,5],"Marks":[23,34,31,25,46]})
    st.write("Generated Data")
    st.dataframe(df)
    csv=df.to_csv(index=False,encoding="utf-8")
    st.download_button("Download csv file",data=csv,file_name="marks.csv",mime="text/csv")