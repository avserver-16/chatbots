# T&C Shortener Bot

A simple AI-powered chatbot that summarizes long documents such as Terms & Conditions, Privacy Policies, agreements, and legal text into clear, easy-to-understand language.

## Features

* Summarize lengthy documents in seconds
* Choose summary detail level:

* Very Short
  * Medium
  * Detailed
* Ask follow-up questions about the document
* Runs completely locally
* No API keys required
* Private and secure

## Tech Stack

* Python
* Streamlit
* Ollama
* Mistral 7B
* LangChain

## Installation

1. Install Ollama
2. Download the Mistral model:

```bash
ollama pull mistral
```

3. Install dependencies:

```bash
pip install streamlit ollama langchain langchain-community
```

4. Run the application:

```bash
streamlit run app.py
```

## Usage

1. Paste a Terms & Conditions document.
2. Select the desired summary level.
3. Click **Summarize**.
4. Review the generated summary.
5. Ask follow-up questions for more clarity.

## Goal

Help users quickly understand complex documents without reading hundreds of lines of legal text.

## Privacy

All processing happens locally on your machine. No document data is sent to external APIs.
