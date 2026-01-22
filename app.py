import streamlit as st

st.title("anketa")
text = st.text_input("vavedi lobimo shivotno")
subject = st.selectbox("животни",
[text , "куче","котка"])
