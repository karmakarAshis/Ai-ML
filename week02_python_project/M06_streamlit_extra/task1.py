import streamlit as st

# title 
st.title("Personal Info Card App", anchor=False)
st.divider()

# taking user info
name = st.text_input("Enter Your name")
age = st.number_input("Enter Your age", value=None)
profession = st.selectbox("Choose Your profession",
             ("Student", "Employee", "Businessman", "Freelancer"), index=None)


button_pressed = st.button("Show information")

# checking and required field
if not name or not age or not profession:
    st.warning("all field are required")
else:
    st.success("Success")


# display information
if button_pressed:
    st.write(f"Your name is {name}, a {age} years old {profession}.")