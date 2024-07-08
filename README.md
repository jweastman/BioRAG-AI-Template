# RAG Application Template

## What is a RAG Application?
A Retrieval-Augmented Generation (RAG) application is a type of AI-powered system that combines the capabilities of retrieval-based models 
and generation-based models. The main goal of a RAG application is to enhance the quality and accuracy of generated content by incorporating relevant 
information retrieved from a vast knowledge base. This approach leverages the strengths of both retrieval and generation, providing more coherent and contextually appropriate outputs.

## About this template
This project shows how to create an application using streamlit which is then hosted on Domino. We are using an Azure OpenAI embedding model to create the emebeddings of our documents and
a gpt model (GPT-4, GPT-4o, etc.) as the base model. 

The important files in this template are:
* [.env](https://github.com/jweastman/BioRAG-AI-Template/blob/main/.env): Our environment file, a simple text file used to set environment variables.
* [utils.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/utils.py): This file contains utility functions that are used throughout the codebase.
* [base_agent.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/base_agent.py): This file defines a BaseAgent class that initializes a chat model and embeddings using Azure's OpenAI services, configured with environment variables for deployment and API access.
* [UseCases.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/UseCases.py): The page on the streamlit application for use case management.
* [pages/Chatbot.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/pages/Chatbot.py): The chatbot interface on the application where users can select their use case and speak with BioRAG.
* [app.sh](https://github.com/jweastman/BioRAG-AI-Template/blob/main/app.sh): The script needed to run the app.

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
 RUN pip install azure-storage-blob==12.20.0
```
