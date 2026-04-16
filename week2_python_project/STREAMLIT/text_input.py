import streamlit as st

st.title(":lizard: First WebApps", anchor=False)

st.header("content 1", divider=True)
st.subheader("content 1 sub")

st.text("hello world")

st.markdown(":red[**hello**] *world*")

st.markdown(":red-background[:orange[**hello**] *world*]")

a=10
b=20