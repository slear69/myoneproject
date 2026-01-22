import streamlit as st

st.title("anketa")
text = st.text_input("предмети в училище")
subject = st.selectbox("предмети",
[text , "куче","котка"])
