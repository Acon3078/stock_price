import streamlit as st
import subprocess

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to:", ["Stock Price App", "Other App"])

if option == "Stock Price App":
    st.write("### Welcome to Stock Price App")
    # Run the first script
    subprocess.run(["python", "stock.py"])
elif option == "Other App":
    st.write("### Welcome to My Other App")
    # Run the second script
    subprocess.run(["python", "other_project.py"])
