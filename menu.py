import streamlit as st
import stock
import dna

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to:", ["Stock Price App", "DNA App"])

if option == "Stock Price App":
    stock.main()  # Call the main function from stock.py
elif option == "DNA App":
    dna.main()  # Call the main function from dna.py
