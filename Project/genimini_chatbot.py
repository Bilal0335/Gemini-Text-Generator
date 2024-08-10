import streamlit as st
import google.generativeai as genai
API_KEY = "AIzaSyBbHkLAjGRRhY73L99nQ9siY__8oPgVzRs"
genai.configure(api_key=API_KEY)

# ! Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text


st.title("Gemini Chatbot")
user_input = st.text_input("Enter Your Prompt")
if st.button("Get Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"ChatBot Response: {output}")
    else:
        st.write("PLease enter a prompt.")
        

# print(output)
