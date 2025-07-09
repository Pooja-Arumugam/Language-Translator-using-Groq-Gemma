# Language Translator using Groq Gemma

A sleek, Streamlit-based language translation app powered by **LangChain** and **Groq's Gemma model**. This project enables dynamic text translation between multiple languages using the efficiency of Groq hardware and the intelligence of Gemma LLMs.

## Project Highlights

- Translates text across multiple languages
- Ultra-fast inference with Groq LPU
- Built using LangChain and Groq’s integration for seamless LLM interaction
- Simple and intuitive UI via Streamlit

---

## Tech Stack

| Layer       | Tools / Libraries                             |
|-------------|-----------------------------------------------|
| Frontend    | Streamlit                                     |
| Backend     | LangChain, Groq, Python                       |
| Translation | Gemma LLM (via `langchain_groq`)             |
| API Access  | `.env` for secure API key management          |

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Pooja-Arumugam/Language-Translator-using-Groq-Gemma.git
   cd Language-Translator-using-Groq-Gemma
   ```

2. **Create and Activate Virtual Environment**
 ```bash
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```
3. **Install Required Packages**
```bash
pip install -r requirements.txt
Set Environment Variables
```
4. **Create a .env file in the root directory.**
 ```bash
     Add your Groq API key:
     GROQ_API_KEY=your_api_key_here
```
 5. **Run the Streamlit App**
```bash
     streamlit run app.py
```
