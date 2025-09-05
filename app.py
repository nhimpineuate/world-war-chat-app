import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# try to import generative ai 
try:
    import google.generativeai as genai
except ImportError:
    genai = None    

# Page configuration
st.set_page_config(page_title="World War Chat", page_icon="🇬🇧", layout="wide")

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Settings")
    st.caption("🔑 Provide your API key & tweak generation parameters")
    
    # API key input
    api_key = st.text_input("🔐 GEMINI_API_KEY", type="password", 
                           value=os.getenv("GEMINI_API_KEY", ""))
    
    # Model selection
    model_name = st.selectbox("🤖 Model", 
                              ["gemini-2.0-flash"])

    # System instruction for world war focus
    system_instruction = st.text_area(
        "System instruction",
        value="You are the world war assistant. You only provide information about world war, history, and the causes of the war.",
        height=80
    )

    # Generation parameters
    st.subheader("Generation Parameters")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    top_p = st.slider("Top P", 0.0, 1.0, 0.9, 0.05)
    top_k = st.slider("Top K", 1, 100, 40, 1)
    max_output_tokens = st.slider("Max Output Tokens", 1, 8000, 100, 100)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    st.session_state.chat = None

# Cache the model to avoid recreating it
@st.cache_resource(show_spinner=False)
def get_model(api_key, model_name, system_instruction):
    """Initialize and cache the Gemini model with error handling."""
    if genai is None:
        raise ImportError("google_generativeai is not installed")
    
    if not api_key:
        raise ValueError("API key missing")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name, system_instruction=system_instruction)

# Main app
st.title("🌍 World War History Chat")
st.caption("📚 Welcome to the catalogue of world war history - let's explore together!")

# Display chat history 
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# User input
user_prompt = st.chat_input("Ask me anything about world war")      

# Process user input
if user_prompt:
    # Add user message to history
    st.session_state.messages.append({'role': 'user', 'content': user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Get model
    try:
        model = get_model(api_key, model_name, system_instruction)
    except Exception as e:
        st.error(str(e))
        st.stop()
    
    # Generate configuration
    gen_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
        "response_mime_type": "text/plain",
    }

    # Initialize chat session if needed
    if st.session_state.chat is None:
        history = []
        for msg in st.session_state.messages[:-1]:  # Exclude the current message
            role = "user" if msg["role"] == "user" else "model" 
            history.append({"role": role, "parts": [msg["content"]]})      
        st.session_state.chat = model.start_chat(history=history)

    # Generate response  
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(user_prompt, generation_config=gen_config)
                answer = response.text or '(No text response)'
            except Exception as e:
                answer = f"Error: {e}"
            st.markdown(answer) 

    # Add assistant response to the history
    st.session_state.messages.append({"role": "assistant", "content": answer})
