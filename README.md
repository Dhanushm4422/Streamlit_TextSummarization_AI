echo "# Streamlit Text Summarization AI

This project provides a web application for text summarization using **Streamlit** and **Transformers**. The application allows users to input a paragraph of text, and it will generate a summarized version of the text.

## Features
- **Text Summarization:** Input text is summarized into a shorter, coherent form using the Hugging Face Transformers library.
- **User-friendly Interface:** Streamlit provides an interactive UI where users can easily enter text and view the summary in real-time.

## Technologies Used
- **Streamlit**: For creating the interactive web app.
- **Transformers**: Hugging Face’s pre-trained transformer models for text summarization.
- **Python**: Backend programming language.
- **PyTorch**: Deep learning framework used by the transformer models.

## Setup and Installation

### Prerequisites
- Python 3.7 or above
- Git (optional for cloning repository)

### Steps to Run the Project

1. **Clone the repository:**

   If you don't have the project locally, clone it using Git:
   \`\`\`bash
   git clone https://github.com/Dhanushm4422/Streamlit_TextSummarization_AI.git
   cd Streamlit_TextSummarization_AI
   \`\`\`

2. **Set up a virtual environment (recommended):**
   - You can create a virtual environment to manage project dependencies:
   \`\`\`bash
   python -m venv myenv
   \`\`\`
   - Activate the virtual environment:
     - On Windows:
       \`\`\`bash
       myenv\Scripts\activate
       \`\`\`
     - On macOS/Linux:
       \`\`\`bash
       source myenv/bin/activate
       \`\`\`

3. **Install dependencies:**
   - Install the required packages by running:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

   If you don’t have a `requirements.txt` file, you can create one with the following contents:
   \`\`\`text
   streamlit
   transformers
   torch
   \`\`\`

4. **Run the Streamlit app:**
   - Now you can start the application by running:
   \`\`\`bash
   streamlit run app.py
   \`\`\`

5. **Access the app:**
   - Once the app is running, open your browser and go to:
     \`\`\`
     http://localhost:8501
     \`\`\`

6. **Input text for summarization:**
   - In the app, enter any paragraph or text you want to summarize, and it will display the summarized version.

## Project Structure

- `app.py`: Main Streamlit app script that handles user input and displays the result.
- `requirements.txt`: List of dependencies for the project.
- `summarizer.py`: Python script where the summarization logic resides.
- `README.md`: Project documentation (this file).

