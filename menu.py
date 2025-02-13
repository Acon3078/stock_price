import streamlit as st
import subprocess

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to:", ["Stock Price App", "Bioinformatics DNA Count App"])

if option == "Stock Price App":
    st.write("### Welcome to the Stock Price App")
    # Run the first script
    subprocess.run(["python", "stock.py"])
elif option == "Other App":
    st.write("### Welcome to the Bioinformatics DNA Count App")
    # Run the second script
    subprocess.run(["python", "dna-app.py"])
