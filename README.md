# Dr. AI HealthBot

Dr. AI HealthBot is an AI-powered medical assistant that analyzes user queries and medical images to provide disease recognition, remedies, precautions, and possible treatments. It leverages advanced language models and vector search to deliver context-aware medical advice.

## Features
- Accepts user queries and medical images (e.g., skin conditions)
- Uses multimodal LLMs to recognize diseases from images
- Retrieves relevant medical context from a FAISS vector store
- Provides concise, actionable medical advice
- Streamlit-based interface for easy interaction

## How It Works
1. **Image Encoding:** Converts uploaded images to base64 for model input.
2. **Disease Recognition:** Uses a multimodal LLM to suggest the most likely disease from the image.
3. **Context Retrieval:** Embeds the query and disease caption, then searches a FAISS vector store for supporting medical context.
4. **Final Response:** Calls the LLM again with the query, suspected disease, and retrieved context to generate a detailed medical response.

## Setup
1. **Clone the repository:**
   ```powershell
   git clone <repo-url>
   cd Dr.-AI-Healthbot
   ```
2. **Install dependencies:**
   - Use [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency management:
     ```powershell
     pipenv install
     ```
3. **Set up environment variables:**
   - Set your Groq API key:
     ```powershell
     $env:GROQ_API_KEY="your_groq_api_key"
     ```
4. **Prepare vector store:**
   - Ensure the FAISS vector store is present in `vectorstore/faiss_store/`.
   - Add your medical PDF(s) to the `data/` folder if you wish to expand the context database.

## Usage
1. **Run the Streamlit app:**
   ```powershell
   pipenv run streamlit run interface.py
   ```
2. **Upload an image and enter your medical query.**
3. **Receive AI-generated medical advice.**

## File Structure
- `brain.py` — Core logic for image and query analysis
- `interface.py` — Streamlit web interface
- `voice_doctor.py`, `voice_patient.py` — Voice interaction modules
- `vectorstore/faiss_store/` — FAISS vector database
- `data/` — Medical reference documents (PDFs)
- `Pipfile`, `Pipfile.lock` — Dependency management

## Requirements
- Python 3.8+
- Pipenv
- Streamlit
- groq
- langchain_huggingface
- langchain_community
- FAISS

## Notes
- This tool is for informational purposes only and does not replace professional medical advice.
- Ensure your API keys and sensitive data are kept secure.

## License
MIT License
