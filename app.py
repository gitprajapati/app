import streamlit as st
st.title('Multiplication of 2 numbers')
st.subheader("Enter two numbers or use +/- button")
a=st.number_input('Enter 1st number')
b=st.number_input('Enter 2nd number')
st.write("Multiplication of 2 numbers is = ",a*b)
