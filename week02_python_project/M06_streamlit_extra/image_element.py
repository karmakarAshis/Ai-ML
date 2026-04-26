import streamlit as st

st.title("Input your files", anchor=False)
st.divider()

st.image("image/Untitled1.png")
# st.image("https://unsplash.com/photos/northern-lights-3l3RwQdHRHg")

st.divider()

images = st.file_uploader("Enter your Image",
                 type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)


print(type(images))
if images:
    col = st.columns(len(images))

    for i, per_image in enumerate(images):
        with col[i]:
            st.image(per_image)