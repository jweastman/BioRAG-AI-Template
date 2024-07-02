import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureChatOpenAI


class BaseAgent:
    """
    Base agent to chat with GPT-4 without any particular add-on.
    """

    def __init__(self) -> None:

        self.model = AzureChatOpenAI(
            deployment_name=os.getenv("AZURE_CHAT_DEPLOYMENT_NAME"),
            model=os.getenv("AZURE_CHAT_MODEL"),
            temperature=0,
            openai_api_version=os.getenv("OPENAI_API_VERSION"),
            openai_api_key=os.getenv("AZURE_CHAT_API_KEY"),
            azure_endpoint=os.getenv("AZURE_CHAT_ENDPOINT")
        )

        self.embeddings = AzureOpenAIEmbeddings(
            openai_api_type=os.getenv("OPEN_AI_TYPE"),
            api_key=os.getenv("AZURE_EMBEDDINGS_API_KEY"),
            azure_endpoint=os.getenv("AZURE_EMBEDDINGS_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("OPENAI_API_VERSION")
)
