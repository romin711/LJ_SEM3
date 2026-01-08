import streamlit as st
import time
st.title("Status element demo")
st.warning("This is a warning msg")
st.error("this is an error msg" )
st.info("Useful informations are here")

st.subheader("progress and spinner")

if st.button("start long run"):
    progress=st.progress(0)
    with st.spinner("Processing..."):
        for i in range(100):
            time.sleep(0.3)
            progress.progress(i+1)
    st.success("Task completed")