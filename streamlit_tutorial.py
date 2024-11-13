import streamlit as st

st.title("This is a Title!")

st.write("This is text!")

st.button("Reset", type="primary")
if st.button("Say Hello"):
    st.write("Why hello there!")
    st.balloons()
else:
    st.write("Goodbye!")