"""
Affirmation API Router
This module defines the API endpoints for sending daily affirmations via SMS.
"""

from typing import Optional
from fastapi import APIRouter, Body

from models import CustomMessage
from services.affirmation import AffirmationGenerator
from clients.twilio import TwilioClient
from utils.secrets import VaultSecretsLoader

router = APIRouter(prefix="/v1", tags=["affirmation"])

# Load phone numbers from secrets or environment
AFFIRMATION_NUMBERS = VaultSecretsLoader().load_secret("affirmation-phone-numbers")


@router.post("/send")
def send_message(custom_message: Optional[CustomMessage] = Body(None)):
    """
    Sends a daily affirmation via SMS.
    If a custom message is provided, it will be sent instead of the generated affirmation.
    Args:
        custom_message (CustomMessage): Optional custom message to send.
    Returns:
        dict: A dictionary containing the message SID, body, from number, and to number.
    """
    affirmation_generator = AffirmationGenerator()
    twilio_client = TwilioClient().get_client()

    if custom_message is None:
        body = affirmation_generator.generate()
    else:
        body = custom_message.message

    message = twilio_client.messages.create(
        from_=AFFIRMATION_NUMBERS.get("FROM_NUMBER"),
        body=body,
        to=AFFIRMATION_NUMBERS.get("TO_NUMBER"),
    )

    return {
        "messageSid": message.sid,
        "body": body,
        "from": message.from_,
        "to": message.to,
    }
