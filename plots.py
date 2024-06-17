import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

st.header('charts with random  numbers')

chart_data = pd.DataFrame(np.random.randn(20,3),columns=['line1','line2','line3'])

st.subheader('Line Chart')
st.line_chart(chart_data)

st.subheader('area chart')
st.area_chart(chart_data)

st.subheader('bar chart')
st.bar_chart(chart_data)

st.subheader('Data Visulaziation with matplotlib & Seaborn')
df = pd.read_csv("D:\python\\strramlit\\ref\\iris.csv")
#st.dataframe(df)

st.subheader('2.2 Distrubution plot with matplotlib')
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution plot with seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader('multi graphs')

col1,col2 = st.columns(2)
with col1:
    col1.header = 'kde = False'
    col1.write('kde=False')
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'],kde = False)
    st.pyplot(fig1)

with col2:
    col2.header = 'Hist = False'
    col2.write('kde=False')
    fig2 = plt.figure()
    sns.distplot(df['sepal_length'],hist = False)
    st.pyplot(fig2)

st.header('changing style')
col1,col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist = False)
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure()
    sns.set_theme(context = 'poster',style='darkgrid')
    sns.distplot(df['petal_length'],hist = False)
    st.pyplot(fig2)

st.header('Exploring diferent Graphs')
st.subheader('scatter plot')
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)


st.subheader('count-plot')
fig = plt.figure(figsize=(15,8))
sns.countplot(data = df ,x='species')
st.pyplot(fig)


st.subheader('box-plot')
fig = plt.figure(figsize=(15,8))
sns.boxplot(data = df, x = 'petal_length')
st.pyplot(fig)
