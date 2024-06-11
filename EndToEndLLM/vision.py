from dotenv import load_dotenv
load_dotenv() ## To load all the environment variables

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load Gemini pro model and get response

def get_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input,image])
    else:
         response = model.generate_content(image)
    return response.text

## Streamlit Framework
st.set_page_config(page_title='Gemini Image worker')
st.title('Working on Images with Gemini')
input = st.text_input("Input Prompt:", key='input')
uploaded_image = st.file_uploader("Choose an Image to upload :", type=['jpg', 'png','jpeg'])

image = ""
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded image", use_column_width=True)

submit = st.button('Tell me about this Image')

if submit:
    with st.spinner('Please wait...'):
        response = get_response(input,image)
        st.subheader('The response is:')
        st.write(response)









