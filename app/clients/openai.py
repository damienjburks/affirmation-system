"""
OpenAI Client Module
This module provides a class to interact
with OpenAI's API for generating affirmations.
"""

from openai import OpenAI
from utils.secrets import VaultSecretsLoader


class OpenAIClient:
    """
    A class to interact with OpenAI's API.
    """

    def __init__(self, api_key: str = None):
        if api_key is None:
            loader = VaultSecretsLoader()
            api_key = loader.load_secret("openai-api-token")
        self.client = OpenAI(api_key=api_key)

    def get_client(self):
        """
        Returns the OpenAI client instance.
        """
        return self.client
