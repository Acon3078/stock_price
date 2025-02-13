import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

def main():
    # Page Title
    image = Image.open('dna-logo.jpg')
    st.image(image, use_container_width=True)

    st.write("""
    # DNA Nucleotide Count Web App

    This app counts the nucleotide composition of query DNA!

    ***
    """)

    # Input Text Box
    st.header('Enter DNA sequence')
    sequence_input = """>DNA Query 2
    GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
    ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
    TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"""

    sequence = st.text_area("Sequence input", sequence_input, height=250)
    sequence = sequence.splitlines()
    sequence = sequence[1:]  # Skip sequence name
    sequence = ''.join(sequence)  # Concatenate list to string

    st.write("***")

    # Prints the input DNA sequence
    st.header('INPUT (DNA Query)')
    st.write(sequence)

    # DNA nucleotide count
    st.header('OUTPUT (DNA Nucleotide Count)')

    # Function to count nucleotides
    def DNA_nucleotide_count(seq):
        seq = seq.upper()
        return {
            'A': seq.count('A'),
            'T': seq.count('T'),
            'G': seq.count('G'),
            'C': seq.count('C')
        }

    X = DNA_nucleotide_count(sequence)

    # Display count dictionary
    st.subheader('1. Nucleotide Count Dictionary')
    st.write(X)

    # Display counts as text
    st.subheader('2. Individual Counts')
    st.write(f"There are {X['A']} adenine (A)")
    st.write(f"There are {X['T']} thymine (T)")
    st.write(f"There are {X['G']} guanine (G)")
    st.write(f"There are {X['C']} cytosine (C)")

    # Convert to DataFrame
    st.subheader('3. Display DataFrame')
    df = pd.DataFrame.from_dict(X, orient='index', columns=['count']).reset_index()
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)

    # Display Bar Chart using Altair
    st.subheader('4. Display Bar Chart')
    p = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count'
    ).properties(width=alt.Step(80))  # controls width of bars
    st.write(p)

# Ensure the script can be run independently or as a module
if __name__ == "__main__":
    main()
