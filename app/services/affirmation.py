"""
Afrirmation Generator Service
"""

import logging
from clients.openai import OpenAIClient

AI_PROMPT = """
Act as a motivational coach and wellness guide. 
Generate a short, uplifting daily affirmation (1–2 sentences) that emphasizes the 
power of consistency, regular physical activity, and caring for your overall health. 
The tone should be warm, encouraging, and grounded—ideal for 
someone working to build a habit of daily workouts and long-term wellness.

End each affirmation with a positive nudge (e.g., "You’ve got this" or "One step at a time") 
followed by a personal signature on a new line: "—Love, Damien 💙".
"""


class AffirmationGenerator:
    """
    A class to generate daily affirmations using OpenAI's API.
    """

    def __init__(self):
        self.openai_client = OpenAIClient().get_client()
        self.prompt = AI_PROMPT

    def generate(self) -> str:
        """
        Generates a daily affirmation using OpenAI's API.
        Returns:
            str: A motivational affirmation.
        """
        chat_completion = self.openai_client.chat.completions.create(
            messages=[{"role": "user", "content": self.prompt}],
            model="gpt-4o",
        )
        answer = chat_completion.choices[0].message.content
        logging.info("OpenAI response: %s", answer)
        return answer
