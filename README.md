# RAG Application Template

## License
This template is licensed under Apache 2.0 and contains the following components: 
* Langchain [MIT](https://github.com/langchain-ai/langchain/blob/master/LICENSE)
* [OpenAI](https://openai.com/policies/terms-of-use)


## What is a RAG Application?
A Retrieval-Augmented Generation (RAG) application is a type of AI-powered system that combines the capabilities of retrieval-based models 
and generation-based models. The main goal of a RAG application is to enhance the quality and accuracy of generated content by incorporating relevant 
information retrieved from a vast knowledge base. This approach leverages the strengths of both retrieval and generation, providing more coherent and contextually appropriate outputs.

## About this template
This project provides a template for a streamlit application which is then hosted on Domino. We are using an OpenAI embedding model to create the emebeddings of our documents and
a gpt model (GPT-4, GPT-4o, etc.) as the base model. 

The important files in this template are:
* [.env](https://github.com/jweastman/BioRAG-AI-Template/blob/main/.env): Our environment file, a simple text file used to set environment variables.
* [utils.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/utils.py): This file contains utility functions that are used throughout the codebase.
* [base_agent.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/base_agent.py): This file defines a BaseAgent class that initializes a chat model and embeddings using Azure's OpenAI services, configured with environment variables for deployment and API access.
* [UseCases.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/UseCases.py): The page on the streamlit application for use case management.
* [pages/Chatbot.py](https://github.com/jweastman/BioRAG-AI-Template/blob/main/pages/Chatbot.py): The chatbot interface on the application where users can select their use case and speak with BioRAG.
* [app.sh](https://github.com/jweastman/BioRAG-AI-Template/blob/main/app.sh): The script needed to run the app.

## Setup instructions

### External Services Set Up
Step 1
Ensure you have the following external services set up with the correct credentials provided in the .env file
* Azure blob storage - [Credentials tutorial](https://learn.microsoft.com/en-us/answers/questions/1071173/where-can-i-find-storage-account-connection-string)
* Qdrant Vector Database - [Tutorial](https://qdrant.tech/documentation/quickstart/)
* Azure OpenAI Chat Model Resource - [Deployment Types](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/deployment-types) (See below for Azure OpenAI Keys and Endpoints)
* Azure OpenAI Embeddings Resource - [Deployment Types](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/deployment-types) (See below for Azure OpenAI Keys and Endpoints)

### Location of keys for Azure OpenAI Resources
  ![image](https://github.com/user-attachments/assets/ad50eda1-a1a6-4ca7-9754-c2fdf2d46a54)


Should you require assistance setting these services up, please reach out to Gabriele Oliva from BIP, gabriele.oliva@bip-group.com

### Environment Requirements 
The necessary packages and versions can be found in the requirements.txt file. Ensure these packages are installed in a custom Domino Environment. Please find the docker instructions below:

Step 2
Create a custom environment on Domino with a base environment of Domino Standard Environment

Step 3
Under dockerfile instructions use the instructions provided below to install the python packages into the environment.

 ```
 RUN pip install langchain==0.2.0 --user
 RUN pip install langchain_community==0.2.0 --user
 RUN pip install langchain_openai==0.1.7 --user
 RUN pip install langchain_text_splitters==0.2.0 --user
 RUN pip install pandas==2.2.2 --user
 RUN pip install pdfplumber==0.11.0 --user
 RUN pip install python-dotenv==1.0.1 --user
 RUN pip install qdrant_client==1.9.1 --user
 RUN pip install streamlit==1.33.0 --user
 RUN pip install azure-storage-blob==12.20.0 --user
```
### Hardware Requirements 
Step 4
Utilize small hardware tier requirements  
