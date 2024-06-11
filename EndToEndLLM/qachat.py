from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to get response Gemini pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question, stream=True)
    return response
    
## Streamlit Framework

st.set_page_config(page_title= "Chatbot Gemini Pro")
st.header("Welcome to Gemini Pro Chatbot")

## Initialize session for chat history if not exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] 

## Place holder for text input messages
input = st.text_input("Enter your input:", key='input')

## Button to submit the question
submit = st.button('Ask the question')


if submit and input:
    with st.spinner('Please wait...'):
        response = get_response(input)
        # add the question to your chat_history
        st.session_state['chat_history'].append(("You", input))
        # add the response to your chat_history
        st.subheader('The response is:')
        for chunk in response:
            st.write(chunk.text) 
            st.session_state['chat_history'].append(("Bot", chunk.text))
        
st.subheader('The chat history is:')

#st.write(st.session_state['chat_history'])

for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')



