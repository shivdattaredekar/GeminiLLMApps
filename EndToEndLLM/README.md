# Gemini Pro Chatbot

This project implements a chatbot using Google's Gemini Pro model and Streamlit for the web interface. The chatbot can respond to user queries in a conversational manner, leveraging the capabilities of the Gemini Pro model.




## Features

- Interactive chatbot interface
- Utilizes Google's Gemini Pro model for generating responses
- Maintains chat history for user sessions
- Responsive and user-friendly design

## Installation

### Prerequisites

- Python 3.10 or higher
- Streamlit
- Google Generative AI package

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/shivdattaredekar/GeminiLLMApps/edit/main/EndToEndLLM
    cd gemini-pro-chatbot
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Code Overview

### Dependencies

- `dotenv`: For loading environment variables from a `.env` file.
- `os`: For accessing environment variables.
- `google.generativeai`: For interfacing with Google's Generative AI services.
- `streamlit`: For building the web application interface.

### Main Components

- **Configuration**: The Google Generative AI is configured with an API key.
- **Function to Get Response**: The `get_response` function sends a question to the Gemini Pro model and returns the response.
- **Streamlit Interface**: Streamlit is used to create a user-friendly web interface. It includes a header, text input field, submit button, and displays the chat history.

### Code Breakdown

```python
from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st

# Configure the Gemini Pro model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from the model
def get_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit setup
st.set_page_config(page_title= "Chatbot Gemini Pro")
st.header("Welcome to Gemini Pro Chatbot")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input for user questions
input = st.text_input("Enter your input:", key='input')

# Button to submit the question
submit = st.button('Ask the question')

# Handle question submission
if submit and input:
    with st.spinner('Please wait...'):
        response = get_response(input)
        st.session_state['chat_history'].append(("You", input))
        st.subheader('The response is:')
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader('The chat history is:')
for role, text in st.session_state['chat_history']:
    st.write(f'{role}: {text}')

