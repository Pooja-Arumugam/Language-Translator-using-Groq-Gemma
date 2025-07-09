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
---
## File Structure
```bash
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (add manually)
├── steps involved.txt      # Project execution steps and logic
```
---
## How It Works
1. UI Layer
- The user enters a prompt in Streamlit and selects the target language.

2. Prompt Construction
- A ChatPromptTemplate is created using langchain_core.prompts.

3. Model Selection
- Groq's ChatGroq is initialized with the Gemma model (e.g., gemma-7b-it).

4. Response Handling
- Output is parsed using StrOutputParser and displayed back in the UI.
---
## Key Dependencies
 - streamlit – for UI rendering
 - langchain – for prompt templating and chain logic
 - langchain_groq – Groq model integration
 - python-dotenv – for loading API keys securely
 - os – to handle environment variables

## Future Improvements
 - Add support for speech-to-text and text-to-speech
 - Extend support to more LLM providers (e.g., OpenAI, Mistral)
 - Add translation history and export option

## Acknowledgments
 - Groq for blazing-fast inference
 - LangChain for the intuitive LLM interface
 - Streamlit for making UI development easy
