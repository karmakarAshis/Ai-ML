import streamlit as st

# title 
st.title("Image Gallery App", anchor=False)
st.divider()

# image uploader

images = st.file_uploader("upload your images",
                          type=["jpg", "jpeg", "png"],
                          accept_multiple_files=True)

st.divider()


# showing images
if len(images) > 3:
    st.error("Too many files uploaded")
elif len(images) ==3:
    st.success("successfully uploaded")
  
if len(images) <=3:
    if images:
        col = st.columns(len(images))
        for i, per_image in enumerate(images):
            with col[i]:
                st.image(per_image)







