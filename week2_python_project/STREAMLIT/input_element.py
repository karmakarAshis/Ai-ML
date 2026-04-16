import streamlit as st

st.title("Input your information", anchor=False)
st.divider()

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", value=None)

pressed = st.button("Enter to Confirm")



selected = st.selectbox("choose your profession",
             ("Student", "Employee", "Business"), index=None,
             accept_new_options=True)

print(type(selected))
st.write("you selected ", selected)






if pressed:
    st.write(f"your name is {name} and age is  {age}")



# password = st.text_input("Enter your password", type="password")
# print(type(password))
# st.write("Your name is: ", password)