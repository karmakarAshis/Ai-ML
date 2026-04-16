import streamlit as st

st.title("Input your (video)", anchor=False)
st.divider()

video_file = st.file_uploader("Enter your video",
                 type=['mp4', 'mkv'], accept_multiple_files=False)


button  = st.button("click to uploads")

if button:
    if video_file:
        st.video(video_file)
        st.success("File uploaded Succesfully")
    else:
        st.error("please upload a video file")