"""
Models Module
This module provides Pydantic models for data validation and serialization.
"""

from pydantic import BaseModel


class CustomMessage(BaseModel):
    """
    A Pydantic model for custom messages.
    """

    message: str
