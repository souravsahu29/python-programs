import streamlit as st
st.write("Hello World")
num1 = st.number_input("Num1")
num2 = st.number_input("Num2")
if st.button("Add"):
    st.write(f"# {num1+num2}")
    st.balloons()
st.file_uploader("Upload csv")
st.camera_input("Smile😀")