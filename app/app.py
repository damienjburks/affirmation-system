"""
This file is part of the Affirmation System project.
It is designed to send affirmations via SMS using the Twilio API and
generate them using OpenAI's GPT model.
"""

import logging
import uvicorn
from fastapi import FastAPI
from routers.affirmation_v1 import router as affirmation_router
from utils.cron import DefaultScheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a FastAPI instance
app = FastAPI(
    title="Affirmation System API",
    description="API for sending daily affirmations via SMS using Twilio and OpenAI.",
    version="1.0.0",
    contact={"name": "Damien Burks", "email": "damien@damienjburks.com"},
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)

app.include_router(affirmation_router)

# Start Scheduler
scheduler = DefaultScheduler(interval_hours=24)
scheduler.start()


@app.get("/")
def health_check():
    """
    Health check endpoint to verify the API is running.
    This endpoint returns a simple JSON response indicating the status of the API.
    """
    return {"status": "ok", "message": "Affirmation System is running!"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
        log_level="info",
        use_colors=True,
    )
