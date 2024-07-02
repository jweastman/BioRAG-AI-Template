# RAG Application Template

## What is a RAG Application?
A Retrieval-Augmented Generation (RAG) application is a type of AI-powered system that combines the capabilities of retrieval-based models 
and generation-based models. The main goal of a RAG application is to enhance the quality and accuracy of generated content by incorporating relevant 
information retrieved from a vast knowledge base. This approach leverages the strengths of both retrieval and generation, providing more coherent and contextually appropriate outputs.

## About this template
This project shows how to create an application using streamlit which is then hosted on Domino. We are using Azure OpenAI's `text-embedding-ada-002` model to create the emebeddings of our documents and
OpenAI's `gpt-4-32k` model as the base model. 

The important files in this template are:
* .env: Our environment file, a simple text file used to set environment variables.
* requirements.txt: Requirements file to be used when creating domino 
* utils.py: This file contains utility functions that are used throughout the codebase.
* agent.py: This file defines a BaseAgent class that initializes a chat model and embeddings using Azure's OpenAI services, configured with environment variables for deployment and API access.
* app.py: Streamlit app code.
* app.sh: The script needed to run the app.

## Setup instructions
The necessary packages and versions can be found in the requirements.txt file. Ensure these packages are installed in a custom Domino Environment. Please find the docker instructions below:
 ```
 RUN pip install langchain==0.2.0
 RUN pip install langchain_community==0.2.0
 RUN pip install langchain_openai==0.1.7
 RUN pip install langchain_text_splitters==0.2.0
 RUN pip install pandas==2.2.2
 RUN pip install pdfplumber==0.11.0
 RUN pip install python-dotenv==1.0.1
 RUN pip install qdrant_client==1.9.1
 RUN pip install streamlit==1.33.0
 RUN pip install azure-storage-blob
```
