import streamlit as st

# Set the title of the web page
st.title("Santa Claus Greets You!")

# Display a greeting from Santa Claus
st.write("Ho Ho Ho! 🎅🎄")

# Ask for the user's name
name = st.text_input("What's your name?", "")

# If a name is provided, greet the user
if name:
    st.write(f"Ho Ho Ho, {name}! Merry Christmas! 🎅🎁")
else:
    st.write("Please enter your name to receive a personal greeting.")
