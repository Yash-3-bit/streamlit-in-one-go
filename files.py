import streamlit as st
import pandas as pd

st.subheader('uploading a csv file')

df = st.file_uploader('upload the csv file: ',type=['csv','xlsx'])
if df is not None:
    st.table(df.head())

st.subheader('loading a csv file')
df = pd.read_csv("D:\python\\strramlit\\ref\\iris.csv")
st.table(df)

st.subheader('dealing with images')
i = st.image('D:\python\\strramlit\\ref\\img.png')
img = st.file_uploader('upload the image file : ',type=['png','jpeg'])
if(img) is not None:
    st.image(img)

st.subheader('working with videos')

videos = st.file_uploader('upload a video file : ',type=['mp4','mkv'])
if videos is not None:
    st.video(videos,start_time=0)

st.subheader('working with audio')
audios = st.file_uploader('upload a audio file : ',type=['mp3'])
if audios is not None:
    st.audio(audios)
