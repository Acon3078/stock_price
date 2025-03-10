import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Set page config
st.set_page_config(
    page_title="DNA Nucleotide Counter",
    page_icon="🧬",
    layout="wide"
)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Page Title with custom styling
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='color: var(--primary);'>DNA Nucleotide Count Web App</h1>
            <p style='color: var(--secondary); font-size: 1.1rem;'>
                Analyze the nucleotide composition of your DNA sequence
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Display logo image with center alignment
    try:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = Image.open('dna-logo.jpg')
            st.image(image, width=1200, use_container_width=False)
    except Exception as e:
        st.warning("Logo image not found. Please ensure 'dna-logo.jpg' is in the same directory.")

    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])

    with col1:
        # Input Text Box
        st.markdown("""
            <h2>Enter DNA Sequence</h2>
            <p style='color: var(--secondary);'>Paste your DNA sequence below:</p>
        """, unsafe_allow_html=True)
        
        sequence_input = """>DNA Query 2
        GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
        ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
        TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"""

        sequence = st.text_area("", sequence_input, height=250)
        sequence = sequence.splitlines()
        sequence = sequence[1:]  # Skip sequence name
        sequence = ''.join(sequence)  # Concatenate list to string

    with col2:
        # Display input sequence
        st.markdown("""
            <h2>Input Sequence</h2>
            <div style='background-color: white; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);'>
                <pre style='font-family: monospace; color: var(--secondary);'>{}</pre>
            </div>
        """.format(sequence), unsafe_allow_html=True)

    # DNA nucleotide count
    st.markdown("<h2 style='color: var(--primary);'>Analysis Results</h2>", unsafe_allow_html=True)

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

    # Create three columns for results
    col1, col2, col3 = st.columns(3)

    with col1:
        # Display count dictionary
        st.markdown("""
            <h3>Nucleotide Count</h3>
            <div style='background-color: white; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);'>
                <pre style='font-family: monospace; color: var(--secondary);'>{}</pre>
            </div>
        """.format(X), unsafe_allow_html=True)

    with col2:
        # Display individual counts
        st.markdown("""
            <h3>Individual Counts</h3>
            <div style='background-color: white; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);'>
                <p>There are <strong>{}</strong> adenine (A)</p>
                <p>There are <strong>{}</strong> thymine (T)</p>
                <p>There are <strong>{}</strong> guanine (G)</p>
                <p>There are <strong>{}</strong> cytosine (C)</p>
            </div>
        """.format(X['A'], X['T'], X['G'], X['C']), unsafe_allow_html=True)

    with col3:
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(X, orient='index', columns=['count']).reset_index()
        df = df.rename(columns={'index': 'nucleotide'})
        st.markdown("""
            <h3>DataFrame View</h3>
        """, unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # Display Bar Chart using Altair
    st.markdown("<h2 style='color: var(--primary);'>Visualization</h2>", unsafe_allow_html=True)
    p = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count',
        color=alt.value('#2563eb')
    ).properties(
        width=alt.Step(80),
        height=400
    )
    st.altair_chart(p, use_container_width=True)

# Ensure the script can be run independently or as a module
if __name__ == "__main__":
    main()
