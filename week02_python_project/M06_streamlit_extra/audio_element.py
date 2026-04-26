import streamlit as st

st.title("Input your (Image)", anchor=False)
st.divider()


st.audio("audio/audio123.mp3", loop=False)

st.divider()

audio = st.file_uploader("Enter your audio",
                 type=['mp3', 'ogg', 'flac'], accept_multiple_files=False)

if audio:
    st.audio(audio)
