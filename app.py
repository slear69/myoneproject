import streamlit as st

st.title("anketa")
age = st.number_input("ваведи години")
name = st.text_input("ваведи име")
subject = st.selectbox("предмети",
["математика" , "булгарски език" , "география","компятарно","физика","химия"])
if st.button("краи"):
  st.success('готово')
  st.write("ти си",name,"на",age,"s lobim predmet",subject,)
