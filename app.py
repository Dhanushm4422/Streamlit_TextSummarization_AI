import streamlit as st
from transformers import pipeline

# Load the pre-trained summarization model
summarizer = pipeline("summarization")

# Streamlit UI (User Interface)
st.title("Text Summarization Tool")
st.write("Enter some text below, and the model will summarize it.")

# Text input area where users can enter their text
input_text = st.text_area("Enter Text to Summarize", "")

# Button to trigger summarization
if st.button("Summarize"):
    if input_text:
        # Call the summarizer to get the summary
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
        st.write("Summary:", summary[0]['summary_text'])
    else:
        st.write("Please enter some text to summarize.")
 