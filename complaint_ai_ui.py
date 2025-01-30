import streamlit as st
import requests

# API URL from Render (Update this after backend deployment)
API_URL = "http://localhost:8000"

st.title("AI-Powered Complaint Summarization & Categorization")
st.write("Enter a customer complaint, and the AI will summarize and categorize it.")

# User Input
complaint = st.text_area("Enter Complaint:", height=150)

if st.button("Process Complaint"):
    if complaint.strip():
        # API request
        response = requests.post(f"{API_URL}/process", json={"complaint": complaint})
        
        if response.status_code == 200:
            result = response.json()
            
            # Display results
            st.subheader("Summarized Complaint:")
            st.write(result["summary"])
            
            st.subheader("Complaint Category:")
            st.write(result["category"].capitalize())
        else:
            st.error("Error processing complaint. Please try again.")
    else:
        st.warning("Please enter a complaint.")
