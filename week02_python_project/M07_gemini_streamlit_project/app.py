import streamlit as st
from PIL import Image
from api_calling import note_generator, audio_transcription, quiz_generator

st.title("Note summary and Quiz Generator", anchor=False)
st.markdown("upload upto 3 images to generate note summary and quizes")
st.divider()

with st.sidebar:
    st.header("controls")
    # image
    images = st.file_uploader(
            "upload the photos of your notes",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True
        )
    pil_images = [Image.open(img) for img in images]


    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("uploaded images")
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)


    # difficulty
    difficulty_options = st.selectbox(
            "Choose the difficulty of your quiz",
            ("Easy", "Medium", "Hard"),
            index=None
        )
    
    pressed = st.button("click the button to initiate AI", type="primary")


if pressed:
    if not images:
        st.error("you must upload a image")
    if not difficulty_options:
        st.error("you must select a difficulty")

    if images and difficulty_options:
        # note container
        with st.container(border=True):
            st.subheader("Your Note", anchor=False)
            
            with st.spinner("AI is writing notes for you"):
                generated_text = note_generator(pil_images)
                st.markdown(generated_text)


        # audio transcript
        with st.container(border=True):
            st.subheader("Your Audio", anchor=False)

            with st.spinner("AI is Generating audio for you"):

                # clearing markdown
                generated_text = generated_text.replace("#", "")
                generated_text = generated_text.replace("*", "")
                generated_text = generated_text.replace("-", "")
                generated_text = generated_text.replace("`", "")
                generated_text = generated_text.replace("\"", "")
                generated_text = generated_text.replace("\'", "")
                generated_text = generated_text.replace("_", "")
                generated_text = generated_text.replace("(", "")
                generated_text = generated_text.replace(")", "")
                generated_text = generated_text.replace("{", "")
                generated_text = generated_text.replace("}", "")

                audio_transcript = audio_transcription(generated_text)
                st.audio(audio_transcript)


        # quize container
        with st.container(border=True):
            st.subheader(f"Quiz ({difficulty_options}) level", anchor=False)

            with st.spinner("AI is creating Quizes for you"):
                quizes = quiz_generator(pil_images, difficulty_options)
                st.markdown(quizes)

