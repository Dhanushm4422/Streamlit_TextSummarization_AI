from transformers import pipeline

# Load the pre-trained summarization model from Hugging Face
summarizer = pipeline("summarization")

def summarize_text(text):
    # Summarize the text using the Hugging Face model
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    text = """
    Your long article or paragraph goes here. For example, GPT-3 by OpenAI is an autoregressive language model
    that uses deep learning to produce human-like text. It has been trained on vast amounts of text data and is used 
    for tasks like text generation, translation, summarization, and more.
    """
    
    # Call the summarize function
    summary = summarize_text(text)
    print("Summary:", summary)
