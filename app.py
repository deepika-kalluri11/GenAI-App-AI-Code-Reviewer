import os
import streamlit as st
import google.generativeai as genai

# Configure the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key is set
if not api_key:
    st.error("API Key is missing! Set the GOOGLE_API_KEY in your environment.")
else:
    genai.configure(api_key=api_key)

# Function to call the API for code review
def review_code(code):
    model = genai.GenerativeModel("gemini-pro")  # This can be adjusted or replaced with a different model if necessary
    response = model.generate_content(f"Analyze this Python code and provide feedback on bugs and improvements:\n\n{code}")
    return response.text  # Get the response as text

# Function to get a fixed version of the code
def get_fixed_code(code):
    model = genai.GenerativeModel("gemini-pro")  # Same as above
    response = model.generate_content(f"Fix any errors in this Python code and return a corrected version:\n\n{code}")
    return response.text

# Streamlit UI
st.title("🧑‍💻 AI Code Reviewer")

# Code input box
code = st.text_area("Enter your Python code here:", height=200)

# Review button
if st.button("Review Code"):
    if not code.strip():
        st.warning("Please enter some code to review.")
    else:
        with st.spinner("Analyzing your code..."):
            feedback = review_code(code)
            fixed_code = get_fixed_code(code)

        st.subheader("🔍 AI Feedback:")
        st.write(feedback)

        st.subheader("✅ Fixed Code:")
        st.code(fixed_code, language="python")
