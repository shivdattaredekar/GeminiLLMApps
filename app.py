import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import pathlib
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to generate content based on transcript

prompt = """
You are an expert youtube video summarizer. when i will give you the transcript of the video you have to 
summarize the script very well in your own words. you need to tell me what were the important topics that 
were discussed in the video. do not summarize more than 200 words. the transcript text will be appended
here : """
def generate_content(transcript, prompt):
    # Calling the model
    model = genai.GenerativeModel('gemini-pro')
    response  = model.generate_content(transcript + prompt)
    return response.text


# To Fetch transcript information from YT videos

def Extract_Transcript_details(url):
    try:
        video_id = url.split('=')[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript = transcript + i['text'] + "\n"
        return transcript
    
    except Exception as e:
        raise e    


# Streamlit Framework
st.set_page_config('YT video summary')
st.title("YouTube Video Transcript Summarization")

url = st.text_input("Enter the Youtube Video URL")
submit = st.button('Get the Summary')

if url:
    video_id = url.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if submit:
    with st.spinner('Please Wait...'):
        transcript = Extract_Transcript_details(url)
        if transcript:
            response = generate_content(transcript, prompt)
            st.subheader('The Response is:')
            st.write(response)

