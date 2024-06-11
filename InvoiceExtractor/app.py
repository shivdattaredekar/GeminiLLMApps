from dotenv import load_dotenv

load_dotenv() # loads all environment variables

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load gemeni model
model = genai.GenerativeModel('gemini-pro-vision')

# To get the response from the LLM
def get_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text 

# To process the image and convert the data into bytes
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")    


## Streamlit framework
st.set_page_config(page_title='Multilanguage Invoice Extractor')
st.title('Multilanguage Invoice Extract')
input = st.text_input('Input Prompt:',key = 'input')
submit = st.button('Tell me about the invoice')
uploaded_image = st.file_uploader("Choose an image to invoice..." ,type=['jpg', 'png', 'jpeg'])


if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

input_prompt = """
You are expert in understanding the invoices. we will upload the images and 
you will have to answer the questions
that we asked from these uploaded invoice images
"""

if submit:
    with st.spinner('Please wait...'):
        image_data = input_image_setup(uploaded_image)
        response = get_response(input, image_data, input_prompt)
        st.subheader('The Response is:')
        st.write(response)
        st.balloons()





