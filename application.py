import streamlit as st
st.title("welcome to streamlit")

name = st.text_input("enter your name")

clicked = st.button("enter")

if clicked and name:
    st.write(f"hello, {name}!welcome to streamlit")
    st.balloons()
else:
    if name:
        st.write(f"hi, {name}!click below for a surprise")
    else:
        st.write("type your name above,then click below button")