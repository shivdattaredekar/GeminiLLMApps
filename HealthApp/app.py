# load environment variables
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro-vision')

# Function to get response from LLM model
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

# Streamlit Framework

st.set_page_config('Helath App')
st.header('Google Gemini Health App')

input = st.text_input('Input Prompt:')

input_prompt = """
You are health expert and you are expert in calculating the calories of the foods you see.
i will upload the images of meals and then you need to see these images and tell me how much will be total calories of this meal.
along with this i want calories sepraterly for each item in the photo  
"""

uploaded_image = st.file_uploader('Please upload the image to see calories information.', type=['jpg', 'png', 'jpeg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button('Get the information about the Meal')

if submit:
    with st.spinner('Please wait...'):
        image_data = input_image_setup(uploaded_image)
        response = get_response(input, image_data, input_prompt)
        st.subheader('The Response is:')
        st.write(response)
        st.balloons()
