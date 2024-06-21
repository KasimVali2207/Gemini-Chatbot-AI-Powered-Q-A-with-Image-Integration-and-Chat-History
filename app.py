from dotenv import load_dotenv
import streamlit as st
from PIL import Image as PILImage  # Rename to avoid conflicts
import google.generativeai as genai
import io
import os

# Load environment variables from .env file
load_dotenv()

# Configure generativeai with your API key from environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-pro')

# Function to generate response based on input
def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return None

# Streamlit page configuration
st.set_page_config(page_title="Q&A Demo")

# Streamlit application code
st.title("Gemini LLM Application")

# Input text box
input_text = st.text_area("Input:", key="input", height=100)

# Submit button
submit = st.button("Submit")

# Handle submission
if submit:
    if input_text.strip():  # Check if input is not empty
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_text)
            if response:
                st.subheader("Response:")
                st.write(response)
    else:
        st.warning("Please enter a question before submitting.")

# Optional: Add more features such as file upload, styling, additional UI elements, etc.
