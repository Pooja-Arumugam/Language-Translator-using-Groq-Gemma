import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Init model and parser
model = ChatGroq(model="Gemma2-9b-it", groq_api_key=groq_api_key)
parser = StrOutputParser()

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following into {language}:"),
    ("user", "{text}")
])

# Chain
chain = prompt | model | parser

# Set Streamlit config
st.set_page_config(page_title="LangChain Translator 🌐", page_icon="🌍", layout="centered")

# ---------- CUSTOM STYLING: Background + Font ----------
st.markdown("""
    <style>
    body {
        background-color: #f3e5f5;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    <div class="main">
""", unsafe_allow_html=True)



# ---------- CUSTOM TITLE ----------
st.markdown("""
    <h1 style='
        text-align: center; 
        color: #0077cc; 
        font-family: "Trebuchet MS", sans-serif;
        font-size: 38px;
        margin-bottom: 0;
    '>
        🌍 LangChain Translator using GROQ + Gemma
    </h1>
    <p style='text-align: center; font-size: 18px; color: #555;'>Instant translation using LLMs</p>
""", unsafe_allow_html=True)

# ---------- SIDEBAR IMAGE ----------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/512px-React-icon.svg.png", width=120, use_container_width=False)
    st.markdown("#### Powered by LangChain + GROQ")

# ---------- FORM UI ----------
language = st.selectbox("Choose target language", ["French", "Spanish", "German", "Italian", "Japanese","Hindi","Kannada"])
text = st.text_area("Enter text to translate (English)", height=150)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            response = chain.invoke({"language": language, "text": text})
            st.success("Translation:")
            st.text_area("Translated Text", value=response, height=150, key="output_text")

# ---------- ENDING DIV ----------
st.markdown("</div>", unsafe_allow_html=True)
