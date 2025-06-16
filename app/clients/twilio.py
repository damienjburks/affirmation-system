"""
Twilio Client Module
This module provides a class to interact
with Twilio's API for sending SMS messages.
"""

from twilio.rest import Client
from utils.secrets import VaultSecretsLoader


class TwilioClient:
    """
    A class to interact with Twilio's API.
    """

    def __init__(self, account_sid: str = None, auth_token: str = None):
        if account_sid is None or auth_token is None:
            loader = VaultSecretsLoader()
            twilio_credentials = loader.load_secret("twilio-credentials")
            if twilio_credentials:
                account_sid = twilio_credentials.get("ACCOUNT_SID")
                auth_token = twilio_credentials.get("AUTH_TOKEN")
            else:
                raise ValueError("Twilio credentials not found in secrets.")
        self.client = Client(account_sid, auth_token)

    def get_client(self):
        """
        Returns the Twilio client instance.
        """
        return self.client
