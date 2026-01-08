import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.title("Display Data")
data={"student":[1,2,3,4,5],"marks":[12,23,13,14,15],"passed":[True,True,False,True,False]}
df=pd.DataFrame(data)
st.dataframe(df)
st.table(data)
st.json(data)
st.image("img1.avif")

# matplot 
st.header("line chart")
x=np.arange(1,11)
y=np.random.randint(50,100,size=10)
plt.figure(figsize=(6,4))
plt.plot(x,y,marker="o")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line graph")
st.pyplot(plt)

plt.clf()# to avoid overlapping of plots
plt.bar(x,y,color="red")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("bar graph")
st.pyplot(plt)

plt.clf()# to avoid overlapping of plots
plt.scatter(x,y,color="red",marker="d")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("scatter plot")
st.pyplot(plt)

plt.clf()
data=[1,3,6,6,12,12,3,12,8,9,9,8,6,6]
plt.hist(data)
st.pyplot(plt)
plt.clf()

# demo of streamlit charts
st.header("streamlit charts")
chart_data=np.column_stack((x,y))
st.write(chart_data)

st.line_chart(chart_data)
st.line_chart(y)

st.area_chart(chart_data)

st.subheader("bar chart streamlit")

c,b=np.histogram(y,bins=10)
st.write(c,b)
st.bar_chart(c)
st.bar_chart(y)
