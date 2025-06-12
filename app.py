## Conversational Q&A Chatbot using Groq
import streamlit as st
from dotenv import load_dotenv
import os

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq  

# Load API key from .env file
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat!")

# Initialize chat model using Groq
chat = ChatGroq(temperature=0.5, model_name="llama3-8b-8192")  

# Session state to maintain chat history
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a smart AI assistant.")
    ]

# Function to get response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# Input and submit
input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# If button is clicked
if submit and input:
    response = get_chatmodel_response(input)
    st.subheader("The Response is")
    st.write(response)
