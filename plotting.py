import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px

#altair scatter plot
st.header('1. Altair scatter plot')
chart_data = pd.DataFrame(np.random.randn(500,5),columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a',y='b',size='c',
        tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

#intractive charts
st.header('Intractive Chart')
df = pd.read_csv("D:\python\\strramlit\\ref\\lang_data.csv")
lang_lists = df.columns.tolist()
lang_choices = st.multiselect("choose your language" , lang_lists)
new_df = df[lang_choices]
st.line_chart(new_df)
st.subheader('area chart')
st.area_chart(new_df)


#data visualization using plotly
st.header('data visualization with plotly')
df = pd.read_csv("D:\python\\strramlit\\ref\\tips.csv")
st.dataframe(df.head())

#piechart
st.subheader('pie chart')
fig = px.pie(df, values = 'size',names = 'sex',opacity=.9,
             color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

#histogram
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels = ['group-1','group-2','group-3']
fig = ff.create_distplot(hist_data,group_labels,bin_size = [.1,.25,.5])
st.plotly_chart(fig)
