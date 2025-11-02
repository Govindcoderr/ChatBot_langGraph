## 🧠 DocuMind AI — Intelligent Chatbot using LangChain & Ollama
   #### 📘 Description

DocuMind AI is a lightweight intelligent chatbot built with LangChain, Ollama, and LangGraph. It uses the llama3.2:1b model to process user input and generate conversational responses. The project demonstrates how to build a state-based chatbot pipeline using LangGraph’s StateGraph and LangChain’s LLM integration.

This is the foundation of a Retrieval-Augmented Generation (RAG)-ready chatbot that can later be expanded to handle document-based question answering from multiple uploaded files (PDF, Word, Text).

#### 🚀 Features

🧩 Built with LangChain + Ollama for natural language generation

⚡ Uses LangGraph StateGraph for managing chatbot flow

💬 Interactive CLI interface

🦙 Runs locally with Llama 3.2 (1B) model

🧠 Easily extendable for RAG-based document QA

#### 🛠️ Tech Stack

Python 3.10+

LangChain

LangGraph

Ollama

Llama 3.2 (1B) model

#### 📂 Project Structure
App.py            # Main chatbot application

#### ⚙️ Setup Instructions
Install Ollama
```
Download and install Ollama from https://ollama.ai
.
```
Pull the Llama 3.2 model
```
ollama pull llama3.2:1b

```
Create a virtual environment
```
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows

```
#### Install dependencies
```
pip install langchain langchain-ollama langgraph

```
##### Run the chatbot
````
python App.py
````
#### 💻 Usage Example
🤖 Chatbot is ready! Type 'exit' to quit.

You: Hello, who are you?
Bot: I’m DocuMind AI, your intelligent chatbot powered by Llama 3.2!

You: Tell me a joke.
Bot: Why did the developer go broke? Because he used up all his cache!

#### 🧩 Code Explanation

ChatState defines the structure for input/output messages.

chatbot_node processes user input through the Ollama model and returns the generated response.

StateGraph connects the chatbot node with a clear start and end flow.

Main loop runs an interactive console-based chat session.

#### 🧠 Future Enhancements

📚 Add document upload (PDF, Word, Text) support

🔍 Integrate ChromaDB for vector search

🤖 Implement RAG pipeline for context-aware document queries

🌐 Build Gradio UI for user interaction
