from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure generativeai with your API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel for chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to get response from Gemini
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app configuration
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

# Text input for user's question
input_question = st.text_input("Input your question:", key="input")

# Button to submit the question
submit_button = st.button("Ask the question")

# Handle question submission
if submit_button and input_question:
    # Get response from Gemini
    response_chunks = get_gemini_response(input_question)
    
    # Display response
    st.subheader("Response:")
    for chunk in response_chunks:
        st.write(chunk.text)
        st.markdown("---")  # Separator between chunks

    # Display chat history (optional)
    st.subheader("Chat History:")
    for message in chat.history:
        st.text(f"{message['user']}: {message['message']}")

# Optionally, you can add more features and improve code readability as needed.
